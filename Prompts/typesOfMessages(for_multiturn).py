from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="qwen/qwen3.8-27b",
    temperature=0,
    max_tokens=100
)

messages =[
    SystemMessage(content="you are a helpful assistant"),
    HumanMessage(content="tell me about langchain")
]

result = model.invoke(messages)
print(result.content)

messages.append(AIMessage(content=result.content))
print(messages)