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
    {"role": "user", "content": "점심메뉴 추천해줘"}
  ]
)

print(completion.choices[0].message)