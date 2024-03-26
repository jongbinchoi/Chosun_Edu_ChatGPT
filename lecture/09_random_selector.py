from langchain_openai import ChatOpenAI
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import os
from dotenv import load_dotenv, find_dotenv #.env 파일에서 환경 변수를 로드 하는데 사용
from langchain.callbacks import StreamingStdOutCallbackHandler # AI의 답변 생성 과정을 실시간으로 출력하는 콜백 핸들러
from langchain.prompts.example_selector.base import BaseExampleSelector


_ = load_dotenv(find_dotenv()) 

#1. 모델 생성
chat = ChatOpenAI(
    openai_api_key = os.getenv("OPENAI_API_KEY"), 
    temperature=0.1,
    #답변 생성하는과정을 시각화 가능
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)

#ctrl + K+F : 코드 정리
examples = [
    {
        "question": "What do you know about France?",
        "answer": """        
        Here is what I know:        
        Capital: Paris        
        Language: French        
        Food: Wine and Cheese        
        Currency: Euro        """,
    },
    {
        "question": "What do you know about Italy?",
        "answer": """        
        I know this:        
        Capital: Rome        
        Language: Italian        
        Food: Pizza and Pasta        
        Currency: Euro        """,
    },
    {
        "question": "What do you know about Greece?",
        "answer": """        
        I know this:       
        Capital: Athens        
        Language: Greek        
        Food: Souvlaki and Feta Cheese        
        Currency: Euro        """,
    },
]

example_prompt =PromptTemplate.from_template(
    "Human: {question}\nAI:{answer}",
)

prompt = FewShotPromptTemplate(
    example_prompt=example_prompt,
    #examples=examples, 전체 예제 모두 활용
    example_selector=example_selector, #랜덤하게 예제 선택 활용
    suffix="Human: What do you know about {country}?",
    input_variables=["country"],
)

chain = prompt | chat
chain.invoke({
    "country": "vietnam"
})

#RandomSelector 설계 
class RandomExampleSelector(BaseExampleSelector):
    def __init__(self, examples):
        self.examples = examples
    
    def add_example(slef,example):
        self.examples.append(example)
    
    def select_examples(self, input_variables):
        from random import choice
        return [choice(self.examples)]
    
    #RanddomExampleSelector 생성
    example_selector = RandomExampleSelector(examples=examples)
