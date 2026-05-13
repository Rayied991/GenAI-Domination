from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI

model=ChatMistralAI(model= "mistral-small-2506",temperature=0.9)

res= model.invoke("Write a poem on AI")

print(res.content)