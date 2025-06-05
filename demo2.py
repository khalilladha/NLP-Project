from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
import getpass
import os




load_dotenv()
## OpenAI API Key
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")



if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-4o-mini", model_provider="openai")


from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
model.invoke([HumanMessage(content="Hi! I'm Khalil")])

model.invoke([HumanMessage(content="What's my name?")])

model.invoke(
    [
        HumanMessage(content="How are you ?"),
        AIMessage(content="What is your name"),
        HumanMessage(content="My name is khalil"),
        AIMessage(content="Great, how may I help you"),
        HumanMessage(content="What is my name"),
    ]
            
)

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

memory = MemorySaver()
workflow = StateGraph(state_schema=MessagesState)

from typing import Annotated

from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages

from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()



class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)


llm = init_chat_model("gpt-4o-mini")


def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}


# The first argument is the unique node name
# The second argument is the function or object that will be called whenever
# the node is used.
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph = graph_builder.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "1"}}



def stream_graph_updates(user_input: str):
      events = graph.stream(
      {"messages": [{"role": "user", "content": user_input}]},
      config,
      stream_mode="values",)
      for event in events:
          event["messages"][-1].pretty_print()


while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        stream_graph_updates(user_input)
    except:
        # fallback if input() is not available
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        stream_graph_updates(user_input)
        break

