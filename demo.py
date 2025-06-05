import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
load_dotenv()
from langchain_community.llms import Ollama

#os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
llm_model=ChatOpenAI(model='gpt-4o-mini')
st.title("Open AI Model")
key=st.text_input("Please enter your OpenAI Key")
input=st.text_input("Enter your prompt")
if key and input:
    os.environ['OPENAI_API_KEY']=key
    result=llm_model.invoke(input)
    st.text_area("Response", str(result))

   
   

