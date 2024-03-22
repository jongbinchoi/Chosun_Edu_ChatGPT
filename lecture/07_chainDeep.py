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

chef_prompt = ChatPromptTemplate.from_messages([
        ("system", "당신은 전세계에서 유명한 요리사입니다.찾기쉬운 재료를 사용해서 모든 종류의 요리에 대해 쉽게 따라할 수 있는 레시피를 만들어주세요."),
        ("human","나는{cook}요리를 만들고 싶어요!")
])

# chain 1 생성(=>음식 종류)
chef_chain = chef_prompt | chat

veg_chef_prompt = ChatPromptTemplate.from_messages([
        ("system", "당신은 전통적인 요리법을 채식으로 만드는채식주의 요리사 입니다. 대체 재료를 찾고 그 준비과정을 설명하세요. 근복적으로 레시피를 수정하지는 말고, 대체재료가 없는 경우 없다고 하세요."),
        ("human","{recipe}")
])

# chain 2 생성(=>recipe)
veg_chain = veg_chef_prompt | chat


#chain 3 생성(연결)
fainl_chain = {"recipe":chef_chain} | veg_chain #chef_chain의 결과를 veg_chain에 전달, chef_chain json 형태로 전달

#chain 실행
fainl_chain.invoke({ #json 형태로 전달
    "cook":"한식"
})
