from dotenv import load_dotenv

load_dotenv()

## Chatgpt
# from langchain.chat_models import init_chat_model

# model=init_chat_model("gpt-5")
# from langchain_openai import ChatOpenAI
# model=ChatOpenAI(model= "gpt-5")

#gemini
# from langchain.chat_models import init_chat_model

# model=init_chat_model("google_genai:gemini-2.5-flash-lite")

#grok
# from langchain.chat_models import init_chat_model
# model=init_chat_model("groq:openai/gpt-oss-120b")
# from langchain_groq  import  Chatgroq

# model =Chatgroq(model= "openai/gpt-oss-120b")

## Mistral
from langchain_mistralai import ChatMistralAI

# model=ChatMistralAI(model = "mistral-small-2506",temperature=0)
# model=ChatMistralAI(model = "mistral-small-2506",temperature=0.9)
model=ChatMistralAI(model = "mistral-small-2506",temperature=0,max_tokens=20)
print(model)

response = model.invoke("Write a poem on AI")

print(response.content)