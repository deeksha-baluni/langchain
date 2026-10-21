from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel

class student(BaseModel):
    name : str

new_student = {'name' : 'nitish'}

std = student(**new_student)

print(std)