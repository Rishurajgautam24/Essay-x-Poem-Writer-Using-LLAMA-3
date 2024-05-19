from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import ollama
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")

app=FastAPI(
    title="Langchain API",
    version="1.0",
    decsription="A simple LLAMA 3 API Server"
)

llm=Ollama(model="llama3")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words,Well Formatted")
prompt2=ChatPromptTemplate.from_template("Write me an Poem about {topic} with 100 words,Well Formatted")
add_routes(
    app,
    prompt1|llm,
    path="/essay"
)
add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)

