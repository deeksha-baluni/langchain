# you provide a schema (only difference between this and json)from dotenv import load_dotenv

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv

load_dotenv()

# Initialize the Groq Chat Model
model = ChatGroq(
    model="qwen/qwen3.8-27b",
    temperature=1.5,
    # max_tokens=15
)

parser = JsonOutputParser()

template = PromptTemplate(
    template = """
Give me the name, age, and city of a fictional person
{format}
""",
    partial_variables={
        'format': parser.get_format_instructions()
    }
)

prompt = template.format()
result = model.invoke(prompt)

print(result.content)
final = parser.parse(result.content)
print(final['name'])


# again the same can be done with chains

chain = template | model | parser
chain.invoke({})
# invoke should always have something inside it, mostly its 
# input variables, but since there are none so we use blank



