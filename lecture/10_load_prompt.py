from langchain_openai import ChatOpenAI
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.prompts import load_prompt
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

prompt = load_prompt("lecture/data.json")
# prompt = load_prompt("./lecture/data.yaml")


chat = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.1,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)

formatted_prompt = prompt.format(country="Japan")
print(formatted_prompt)
