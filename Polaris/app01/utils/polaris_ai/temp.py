import os
import config
from langchain_community.vectorstores import BaiduVectorDB
from langchain_community.vectorstores.baiduvectordb import ConnectionParams, TableParams
from langchain_community.embeddings import QianfanEmbeddingsEndpoint
from langchain_community.chat_models import QianfanChatEndpoint
from langchain.chains import RetrievalQA

# 初始化向量嵌入和连接参数
embeddings = QianfanEmbeddingsEndpoint()
conn_params = ConnectionParams(
    endpoint=config.endpoint,
    account=config.account,
    api_key=config.api_key
)

# 初始化百度云向量数据库
vector_db = BaiduVectorDB(
    embedding=embeddings,
    connection_params=conn_params,
    table_params=TableParams(384),
    database_name="document",
    table_name="chunks",
    drop_old=False,
)

# 初始化检索器和对话模型
retriever = vector_db.as_retriever(search_type="similarity")
qianfan_chat_model = QianfanChatEndpoint(model="ERNIE-Bot", temperature=0.1)

# 初始化问答模块
qa = RetrievalQA.from_chain_type(llm=qianfan_chat_model, chain_type="refine", retriever=retriever, return_source_documents=True)

# 接收用户输入的问题
query = input("\nYour question: ")

# 处理用户问题并获取答案和相关文档
res = qa(query)
answer, docs = res['result'], res['source_documents']

# 打印用户提出的问题和系统给出的回答
print("\n\n> Question:")
print(query)
print("\n> Answer:")
print(answer)