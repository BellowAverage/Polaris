import time
import pymochow  # 导入pymochow库，用于操作数据库
from pymochow.configuration import Configuration  # 用于配置客户端
import config  # 导入配置文件，包含身份验证和终端信息

# 导入pymochow模型相关的类和枚举类型
from pymochow.model.schema import Schema, Field, VectorIndex, SecondaryIndex, HNSWParams
from pymochow.model.enum import FieldType, IndexType, MetricType, TableState
from pymochow.model.table import Partition

# 使用配置文件中的信息初始化客户端
config_obj = Configuration(credentials=config.credentials, endpoint=config.endpoint)
client = pymochow.MochowClient(config_obj)

# 选择或创建数据库
db = client.database("document")

# 定义数据表的字段
fields = [
    Field("id", FieldType.UINT64, primary_key=True, partition_key=True, auto_increment=False, not_null=True),
    Field("text", FieldType.STRING),
    Field("metadata", FieldType.STRING),
    Field("source", FieldType.STRING),
    Field("author", FieldType.STRING, not_null=True),
    Field("vector", FieldType.FLOAT_VECTOR, not_null=True, dimension=384)
]

# 定义数据表的索引
indexes = [
    VectorIndex(index_name="vector_idx", field="vector", index_type=IndexType.HNSW, metric_type=MetricType.L2, params=HNSWParams(m=32, efconstruction=200)),
    SecondaryIndex(index_name="author_idx", field="author")
]

# 尝试创建数据表，捕获并打印可能出现的异常
try:
    table = db.create_table(table_name="chunks", replication=3, partition=Partition(partition_num=1), schema=Schema(fields=fields, indexes=indexes))
except Exception as e:  # 捕获所有类型的异常
    print(f"Error: {e}")  # 打印异常信息

# 轮询数据表状态，直到表状态为NORMAL，表示表已准备好
while True:
    time.sleep(2)  # 每次检查前暂停2秒，减少对服务器的压力
    table = db.describe_table("chunks")
    if table.state == TableState.NORMAL:  # 表状态为NORMAL，跳出循环
        break

# 打印数据表的详细信息
print("table: {}".format(table.to_dict()))

client.close()  # 关闭客户端连接