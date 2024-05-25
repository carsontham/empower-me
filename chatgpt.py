import os
from openai import OpenAI
from dotenv import load_dotenv

import bs4
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter


load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
client = OpenAI()

llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

from langchain_community.document_loaders import TextLoader

loader = TextLoader("./data/data.txt")

# # Load, chunk and index the contents of the blog.
# loader = WebBaseLoader(
#     web_paths=(
#         "https://www.dbs.com.sg/personal/promotion/insurance-retiresavvy?cid=sg:en:cbg:dbs:sem:goo:na:txt:retsv:retiresavvy:dbs-l4-insurance-retiresavvy:na&gad_source=1&gclid=Cj0KCQjwmMayBhDuARIsAM9HM8eVPGL0Kt-ByLv3JEkJeBMQTy8gVme5gLse75UG0XxKisB48qdrBJUaAp4DEALw_wcB&gclsrc=aw.ds",
#     ),
#     bs_kwargs=dict(parse_only=bs4.SoupStrainer(class_=("read-promotion"))),
# )

docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

# Retrieve and generate using the relevant snippets of the blog.
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

rag_chain.invoke("How low can you commit per month?")

for chunk in rag_chain.stream("How low can you commit per month?"):
    print(chunk, end="", flush=True)

####

# from langchain_community.document_loaders import TextLoader

# loader = TextLoader("./data/data.txt")
# loader.load()
