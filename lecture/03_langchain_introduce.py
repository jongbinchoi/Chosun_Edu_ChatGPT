from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # .env 파일을 찾아서 환경변수를 설정

chat = ChatOpenAI(
    openai_api_key = os.getenv("OPENAI_API_KEY"), # 환경변수에서 API 키를 가져옴
    temperature=0.1, # 0.1~1.0 : 0에 가까울수록 사실기반 답변, 1에 가까울수록 높은 창의성
)

messages = [
    SystemMessage(content="너는 탐험가야, 너는 모든 답변을 영어로 해야해."),
    AIMessage(content="Hello, I'm Jongbin"),
    HumanMessage(content="한국과 일본의 거리는얼마인가요? 그리고 너의 이름은 무엇이니?")
]

print(chat.predict_messages(messages))