# wont work cause hugging face does not support/run gpu for free chat models now, they have been given to 3rd party 
# apps, and they run it with credits now.


from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    provider="featherless-ai",
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("where is delhi located?")
print(result.content)