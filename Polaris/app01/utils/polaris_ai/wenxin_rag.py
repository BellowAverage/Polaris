from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain, StuffDocumentsChain
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate


# 构建初始 messages 列表，这里可以理解为是 openai 传入的 messages 参数
messages = [
  SystemMessagePromptTemplate.from_template(qa_template),
  HumanMessagePromptTemplate.from_template('{question}')
]

# 初始化 prompt 对象
prompt = ChatPromptTemplate.from_messages(messages)
llm_chain = LLMChain(llm=llm, prompt=prompt)

combine_docs_chain = StuffDocumentsChain(
    llm_chain=llm_chain,
    document_separator="\n\n",
    document_variable_name="context",
)
q_gen_chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(qa_condense_template))

qa = ConversationalRetrievalChain(combine_docs_chain=combine_docs_chain,
                                  question_generator=q_gen_chain,
                                  return_source_documents=True,
                                  return_generated_question=True,
                                  retriever=retriever)
print(qa({'question': "藜麦怎么防治虫害？", "chat_history": []}))