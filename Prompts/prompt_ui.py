import os
from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()
model = ChatGroq(
    model="qwen/qwen3.8-27b",
    temperature=0,
    max_tokens=100
)

st.header('Reaserach Tool')

# user_input = st.text_input("enter your prompt")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)

# template
template = PromptTemplate(
    template = """
Please summarize the research paper titled "{paper_input}" with the following specifications:

Explanation Style: {style_input}
Explanation Length: {length_input}

1. Mathematical Details:
    - Include relevant mathematical equations if present in the paper.
    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.

2. Analogies:
    - Use relatable analogies to simplify complex ideas.

If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.

Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variables=['paper_input', 'style_input', 'length_input']

)

# fill the placeholder
prompt = template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})

if st.button('summarise'):
    result = model.invoke(prompt)
    st.write(result.content)

# Verify that the key is actually detected
# print("Key found:", bool(os.getenv("GOOGLE_API_KEY")))

# model = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=1.5, max_completion_tokens=150)
# result = model.invoke("Give me 5 indian names.")

# print(result.content)