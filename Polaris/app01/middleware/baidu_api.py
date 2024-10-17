import os
import requests
import json

def load_env():
    """
    从 .env 文件中加载环境变量
    """
    try:
        with open(".env", "r") as f:
            for line in f:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value
    except FileNotFoundError:
        print(".env 文件未找到")


def get_access_token():

    # 指定网址
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={os.environ['WENXIN_API_KEY']}&client_secret={os.environ['WENXIN_SECRET_KEY']}"
    # 设置 POST 访问
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    # 通过 POST 访问获取账户对应的 access_token
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")

def get_completion(prompt: str, access_token, temperature = 0.1):
    """一个封装文心大模型接口的函数，参数为 Prompt，返回对应结果

    Args:
        prompt (str): 模型的输入
        access_token (str): 密匙".
        temperature (int, optional): Defaults to 0.

    Returns:
        response
    """
    # 可以根据官网文档找到不同模型服务对应的 url
    # 地址：https://console.bce.baidu.com/qianfan/ais/console/onlineService
    url = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token={access_token}"
    # 配置 POST 参数
    payload = json.dumps({
        "messages": [
            {
                "role": "user",# user prompt
                "content": "{}".format(prompt)# 输入的 prompt
            }
        ],
        "temperature" : temperature
    })
    headers = {
        'Content-Type': 'application/json'
    }
    # 发起请求
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    # 返回的是一个 Json 字符串
    js = json.loads(response.text)

    return js["result"]

def call_baidu_wenxin(previous):
    # 手动调用函数加载环境变量
    load_env()

    pretrained = '您是一个AI文本补全助手。您通过API调用，帮助用户完成文本。当用户正在输入内容时，您将预测他或她接下来要写的内容。注意，您将仅向用户的文本提供建议，不要返回用户先前已经编写的部分。长度不要超过20个字符。用户先前编写到：'

    input = pretrained + previous

    return get_completion(input, get_access_token())