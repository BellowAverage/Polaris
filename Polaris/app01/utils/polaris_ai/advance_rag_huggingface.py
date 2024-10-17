from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

# 加载文档
loader = TextLoader('python_info.txt', encoding='utf-8')
documents = loader.load()

# 创建拆分器
text_splitter = CharacterTextSplitter(chunk_size=80, chunk_overlap=0)
# 拆分文档
chunks = text_splitter.split_documents(documents)

from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import Chroma

# embedding model: m3e-base
model_name = "moka-ai/m3e-base"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': True}
embedding = HuggingFaceBgeEmbeddings(
                model_name=model_name,
                model_kwargs=model_kwargs,
                encode_kwargs=encode_kwargs,
                query_instruction="为文本生成向量表示用于文本检索"
            )

# load data to Chroma db
db = Chroma.from_documents(documents, embedding)
# similarity search
db.similarity_search("python是什么")

template = '''
        【任务描述】
        请根据用户输入的上下文回答问题，并遵守回答要求。

        【背景知识】
        {{context}}

        【回答要求】
        - 你需要严格根据背景知识的内容回答，禁止根据常识和已知信息回答问题。
        - 对于不知道的信息，直接回答“未找到相关答案”
        -----------
        {question}
        '''

from langchain import LLMChain
from langchain_wenxin.llms import Wenxin
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

# LLM选型
llm = Wenxin(model="ernie-bot", baidu_api_key="baidu_api_key", baidu_secret_key="baidu_secret_key")

retriever = db.as_retriever()
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
qa = ConversationalRetrievalChain.from_llm(llm, retriever, memory=memory)
qa({"question": "藜怎么防治虫害？"})