from typing import TypedDict
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

class review(TypedDict):
    summary: str
    sentiment: str

model = ChatGroq(
    model="qwen/qwen3.8-27b",
    temperature=0,
    max_tokens=100
)


structured_model = model.with_structured_output(review)

result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove.
 Also, the UI looks outdated compared to other brands. 
 Hoping for a software update to fix this.""")

print(result)
print(result['summary'])
print(result['sentiment'])
