import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# THIS IS STATIC chatbot with both using message(ai,human,system) and not using
# where i have given the user all the authority to queston (static)

load_dotenv()

model = ChatGroq(
    model="qwen/qwen3.8-27b",
    temperature=0,
    max_tokens=100
)

# if i dont use message pattern like (ai, sytem, human) its just a genral chat

# while True:
#     user_input = input('You: ')
#     if user_input == 'exit':
#         break
#     result = model.invoke(user_input)
#     print("AI:", result.content)

# this is bad because read theory

# same chatbot can be made with the help of messages(human, ai, system), so that 
# this time we can have tabs upon who wrote which msg

chat_history = [
    SystemMessage(content ='you are a helpful assistant')
]

while True:
    user_input = input('you: ')
    chat_history.append(HumanMessage(content=user_input))

    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI: ', result.content)

print(chat_history)
                        



