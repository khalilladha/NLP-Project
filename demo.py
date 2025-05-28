import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
load_dotenv()


OPENAI_API_KEY="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"
LANGCHAIN_API_KEY="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"
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

