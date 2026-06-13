from flask import Flask, render_template, request
from langchain_groq import ChatGroq
from src.helper import download_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain


app = Flask(__name__)
load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

embeddings = download_embeddings()

index_name = "medical-chatbot-index"
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

chatModel = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.7, max_tokens=2048)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)
question_answer_chain = prompt | chatModel | StrOutputParser()
stuff_documents_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(
    retriever,
    stuff_documents_chain
)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form.get("msg")

    print("MSG RECEIVED:", repr(msg))

    response = rag_chain.invoke({"input": msg})
    return str(response["answer"])

@app.route("/test")
def test():
    """Simple health check endpoint."""
    return "Flask is working!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)