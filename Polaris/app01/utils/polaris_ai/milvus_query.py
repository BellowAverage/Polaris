import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import QianfanEmbeddingsEndpoint
from langchain_community.vectorstores import Milvus
from milvus import default_server
from langchain.text_splitter import RecursiveCharacterTextSplitter

os.environ["QIANFAN_AK"] = "nRBfRGFk6bIBpX6EkaWPNMAI"
os.environ["QIANFAN_SK"] = "W7nGzNWjBpUeoYT9Qn01c2dSn8Fw4dfT"

# 定义URL
WEB_URL = "https://zhuanlan.zhihu.com/p/89354916"
# 使用WebBaseLoader加载HTML
loader = WebBaseLoader(WEB_URL)
docs = loader.load()
# 加载千帆向量模型
embeddings = QianfanEmbeddingsEndpoint()
# 加载递归字符文本分割器
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 384, chunk_overlap = 0, separators=["\n\n", "\n", " ", "", "。", "，"])
# 加载文本
documents = text_splitter.split_documents(docs)
# 存入向量库
vector_db = Milvus.from_documents(
    documents,
    QianfanEmbeddingsEndpoint(),
    connection_args ={"host": "127.0.0.1", "port": default_server.listen_port},
)

query = "周武王建周是哪年"
res = vector_db.similarity_search(query)
print(res)