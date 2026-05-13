from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
model=ChatMistralAI(model= "mistral-small-latest",temperature=0.9)

messages=[
    SystemMessage(content="You are a funny AI agent")
    
]
print("------------ type 0 to exit application -------")
while True:
    prompt=input("You : ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    res= model.invoke(messages)
    messages.append(AIMessage(content=res.content))
    print("Bot : ",res.content)
    
print(messages)    