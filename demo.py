import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
load_dotenv()


#os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
llm_model=ChatOpenAI(model='gpt-4o-mini',temperature=0.7)

st.title("Open AI Model")
input=st.text_input("Enter your prompt")
button=st.button("Click")
if button:
    result=llm_model.invoke(input)
    st.text_area("Response", str(result))

