from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

# Initialize Gemini's embedding model
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=3)

# Embed a single query
# query = "What is the capital of India?"
# vector = embeddings.embed_query(query)

documents = [
    "delhi is th capital of india", 
    "kolkata is in india",
    "i live in kolkata but i like delhi."
]

vector = embeddings.embed_documents(documents)

# print(f"Embedding length: {len(vector)}")  
print(vector[:5])