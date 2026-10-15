import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Verify that the key is actually detected
print("Key found:", bool(os.getenv("GOOGLE_API_KEY")))

model = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=1.5, max_completion_tokens=150)
result = model.invoke("Give me 5 indian names.")

print(result.content)