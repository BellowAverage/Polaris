from milvus import default_server
from pymilvus import connections, utility
 
# 启动
default_server.start()
 
connections.connect(host='127.0.0.1', port=default_server.listen_port)
 
# 检测服务是否正常启动
print(utility.get_server_version())
 
# 停止
# default_server.stop()