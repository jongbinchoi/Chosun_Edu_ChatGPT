from langchain_openai import ChatOpenAI
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.globals import set_llm_cache, set_debug
from langchain.cache import InMemoryCache, SQLiteCache
import os
from dotenv import load_dotenv, find_dotenv #.env 파일에서 환경 변수를 로드 하는데 사용


#Cahcing을 사용하는 이유?
# -> LLM 모델의 생성된 답변을 저장할 수 있음
# -> 반복 된 동일한 질문이 계속되면 새로 생성하지 않고
#    Cache에 저장한 내용을 재사용
# -> 금전적으로 효율

set_llm_cache(InMemoryCache) #메모리에 저장(휘발성)
set_llm_cache(SQLiteCache("cache.db")) #SQLite에 저장(비휘발성)

_ = load_dotenv(find_dotenv()) 


#1. 모델 생성
chat = ChatOpenAI(
    openai_api_key = os.getenv("OPENAI_API_KEY"), 
    temperature=0.1,
    #답변 생성하는과정을 시각화 가능
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)

chat.predict("한국인 들은 순두부찌개를 어떻게 만들어요?")