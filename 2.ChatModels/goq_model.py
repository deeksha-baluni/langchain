import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# Initialize the Groq Chat Model
model = ChatGroq(
    model="qwen/qwen3.8-27b",
    temperature=1.5,
    max_tokens=15
)

# Invoke the model with the cricket poem prompt from the video
result = model.invoke("Write a summary about New delhi.")


# Check why generation ended:
print("Finish Reason:", result.response_metadata.get("finish_reason"))

# Check token usage breakdown:
print("Usage:", result.response_metadata.get("token_usage"))
# Groq directly returns a clean string
print(result.content)