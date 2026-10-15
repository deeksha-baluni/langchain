from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

# Initialize Gemini's embedding model
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

# Embed a single query
query = "What is the capital of India?"
vector = embeddings.embed_query(query)

print(f"Embedding length: {len(vector)}")  # Output vector length: 768
print(vector[:5])