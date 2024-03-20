from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # .env 파일을 찾아서 환경변수를 설정

chat = ChatOpenAI(
    openai_api_key = os.getenv("OPENAI_API_KEY"), # 환경변수에서 API 키를 가져옴
    temperature=0.1, # 0.1~1.0 : 0에 가까울수록 사실기반 답변, 1에 가까울수록 높은 창의성
)

template = PromptTemplate.from_template(
    "{country_a}과 {country_b}의 거리는 얼마인가요?",
)
prompt = template.format(country_a="한국", country_b="일본")

print(chat.predict(prompt))