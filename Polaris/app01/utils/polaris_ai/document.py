
import pymochow
from pymochow.configuration import Configuration
import config  # 导入配置文件

config_obj = Configuration(credentials=config.credentials, endpoint=config.endpoint)
client = pymochow.MochowClient(config_obj)

print(1, client)

try:
    db = client.create_database("document")
    print(2)
except Exception as e:  # 捕获所有类型的异常
    print(3)
    print(f"Error: {e}")  # 打印异常信息
db_list = client.list_databases()
print(4)
for db_name in db_list:
    print(db_name.database_name)
client.close()