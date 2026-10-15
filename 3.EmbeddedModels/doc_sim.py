from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

# Initialize Gemini's embedding model
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]
# Embed a single query
query = "Tell me about virat kohli."
doc_embed = embeddings.embed_documents(documents)
query_embed = embeddings.embed_query(query)

scores =  cosine_similarity([query_embed], doc_embed)[0]

index, score = sorted(list(enumerate(scores)),key = lambda x:x[1])[-1]
print(index, scores)
print(documents[index])
# print(f"Embedding length: {len(vector)}")  # Output vector length: 768
# print(vector[:5])