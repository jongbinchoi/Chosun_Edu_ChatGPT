# openAI API 사용하기
# - platform.openai.com
# 1.API-KEY 발급
# 2. 카드 등록


# 라이브러리 관리
# 1. VENV
# 2. Anaconda


#챗봇  만들기
# -ChatGPT: 서비스 이름(ex: 카카오톡)
# >인공지능 모델: GPT
# https://openai.com/blog/openai-api


from openai import OpenAI
client = OpenAI(api_key="")#생성자 함수

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": ""},
    {"role": "user", "content": ""}
  ]
)

print(completion.choices[0].message)


#OpenAI API 사용해서 챗봇 문제점
# 1. 개발이 어려움(난이도 상) -> 더 쉽게 개발 할 수 있는 something(프레임워크)이 필요!
# 2. 챗봇 개발 완성 -> Bard 모델 변경 -> Bard API 처음부터 개발!!! -> 프레임워크(LLM)

# -> LangChain 프레임워크(코드 동일: 모델 바꾸면서 쉽게 개발 가능)