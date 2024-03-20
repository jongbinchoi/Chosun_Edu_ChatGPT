from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import os
from dotenv import load_dotenv, find_dotenv


_ = load_dotenv(find_dotenv()) 

#1. 모델 생성
chat = ChatOpenAI(
    openai_api_key = os.getenv("OPENAI_API_KEY"), # 환경변수에서 API 키를 가져옴
    temperature=0.1, # 0.1~1.0 : 0에 가까울수록 사실기반 답변, 1에 가까울수록 높은 창의성
)


#2.parser 생성
from langchain.schema import BaseOutputParser
class CommaOutputParser(BaseOutputParser):
    
    def parse(self, text):
        items = text.strip().split(",")
        return list(map(str.strip, items))

p = CommaOutputParser()

# 3. prompt 생성
template = ChatPromptTemplate.from_messages([
    ("system","너는 리스트 생성 기계다. 모든 답변을 콤마로 구분해서 대답해라."),
    ("human", "{question}")
])

# 4. chain 생성
# -모든 요소를 합쳐주는 역할
# - 합쳐진 요소들은 하나의 Chain으로 실행 (하나하나 순서대로 result를 반환할 때 까지)
# -2개 이상의 chain을 연결
chain = template | chat | CommaOutputParser()

# 5. chain 실행(입력 매개변수 : dick type 전달)
result = chain.invoke({
    "max_items" : "5",
    "question": "포켓몬은 무엇인가?"
})
print(result)