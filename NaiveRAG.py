"""
1.手撕rag 使用之前要掌握的所有内容，首先就是文档加载4种加载方式
2.然后是文档分块采用4种分块方式
3.然后是向量数据库的使用，使用FAISS和CHROME这两种
4.然后是检索和生成使用Langchain的组件。
 
"""

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import json
from langchain_community.document_loaders import DirectoryLoader
# 文档加载器
from langchain_community.document_loaders import TextLoader, PyPDFLoader, UnstructuredMarkdownLoader
from langchain_core.embeddings import Embeddings
# 文本分割器
from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter, MarkdownHeaderTextSplitter, NLTKTextSplitter    
# from sentence_transformers import SentenceTransformer
# Embeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

# 向量数据库
from langchain_community.vectorstores import FAISS, Chroma
headers_to_split=[
    ("#", "h1"),
    ("##", "h2"),
    ("###", "h3"),
    ("####", "h4"),
    ("#####", "h5"),
    ("######", "h6"),
]
md_splitter=MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split)

# #text加载然后递归分隔符分块
loader=TextLoader("test.txt")
loaded_docs=loader.load()
splitter=RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=20)
documents=splitter.split_documents(loaded_docs)
# print(documents)
# #pdf加载然后递归分隔符分块
pdf_loader=PyPDFLoader("test.pdf")
pdf_docs=pdf_loader.load()
pdf_documents=splitter.split_documents(pdf_docs)
# print(pdf_documents)
#directory加载然后递归分隔符分块
dir_loader=DirectoryLoader(
    ".",
    "*.txt",
    TextLoader,
)
dir_docs=dir_loader.load()
dir_documents=splitter.split_documents(dir_docs)
#print(dir_documents)


#md加载然后递归分隔符分块
md_loader=TextLoader("test.md")
md_docs=md_loader.load()
#print(md_docs)
md_documents=md_splitter.split_text(md_docs[0].page_content)
#for doc in md_documents:
    #print(doc.metadata)
import numpy as np
from langchain_community.embeddings import OllamaEmbeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vector=embeddings.embed_query("hello world")
vector2=embeddings.embed_query("english")
similarity = np.dot(vector, vector2) / (np.linalg.norm(vector) * np.linalg.norm(vector2))
print(similarity)
vector_store = FAISS.from_documents(md_documents, embeddings)
result=vector_store.similarity_search_with_score("hello world", k=2)
# print(result)

chroma_vector_store = Chroma.from_documents(
    md_documents,
    embeddings,
    collection_name="my_collection",
)
retriever=chroma_vector_store.as_retriever(
    search_kwargs={"k": 2},
    search_type="mmr",
)
result=retriever.invoke("hello world")
# chroma_result = chroma_vector_store.similarity_search_with_score("hello world", k=2, filter={"h2": {"$eq": "第一章：基础语法"}})
# print(chroma_result)

prompt=ChatPromptTemplate.from_messages([
    ("system","你是一个有用的助手来帮助用户精确查找信息，你会根据用户的查询来检索相关的文档内容来回答用户的问题{context}"),
    ("human","{input}"),
])
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser




model=ChatOpenAI(
    model="mimo-v2.5-pro",
    base_url="https://token-plan-cn.xiaomimimo.com/v1",
    api_key="tp-c84r70owhg1twfldrtelgvppbq8ejpc1nkv3df726cb066au",
)
chain={"context":retriever,"input":RunnablePassthrough()}|prompt| model | StrOutputParser()
if __name__ == "__main__":
    response=chain.invoke("第一章什么内容")
    print(response)