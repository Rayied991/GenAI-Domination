from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
model=ChatMistralAI(model= "mistral-small-latest",temperature=0.9)

print("Chose Your AI Mode")
print("press 1 for Angry Mode")
print("Press 2 for funny mode")
print("Press 3 for Sad Mode")

choice=int(input("Tell your Response :- "))

if choice ==1:
    mode= "You are an angry AI agent. You respond aggressively and impatiently."
elif choice ==2:
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif choice ==3:
    mode= "You are a very sad AI agent. You respond in a depressed and emotional tone."        

messages=[
    SystemMessage(content=mode)
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