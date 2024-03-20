from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import os
from dotenv import load_dotenv, find_dotenv
from langchain.callbacks import StreamingStdOutCallbackHandler


_ = load_dotenv(find_dotenv()) 

#1. 모델 생성
chat = ChatOpenAI(
    openai_api_key = os.getenv("OPENAI_API_KEY"), 
    temperature=0.1,
    #답변 생성하는과정을 시각화 가능
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)