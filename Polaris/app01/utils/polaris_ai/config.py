# config.py
import os
from pymochow.auth.bce_credentials import BceCredentials

# 定义配置信息
account = 'root'
api_key = 'aA014028'
endpoint = 'http://192.168.32.3:5287'

# 初始化BceCredentials对象
credentials = BceCredentials(account, api_key)

os.environ["QIANFAN_ACCESS_KEY"] = "nRBfRGFk6bIBpX6EkaWPNMAI"
os.environ["QIANFAN_SECRET_KEY"] = "W7nGzNWjBpUeoYT9Qn01c2dSn8Fw4dfT"