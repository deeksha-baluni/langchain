from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
load_dotenv()


llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    pipeline_kwargs=dict(
        temperature = 0.5,
        return_full_text = False
        # max_new_tokens = 100
    )
)

model = ChatHuggingFace(llm=llm)

# 1st prompt -> detailed report

temp1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=['topic']
)


#  2nd prompt -> write a 5 line summary 

temp2 = PromptTemplate(
   template=(
           "Task: Summarize the following text into exactly 5 bullet points.\n\n"
           "Text:\n'''\n{text}\n'''\n\n"
           "Bullet Point Summary:"
       ),
    input_variables=['text']
)

prompt1 = temp1.invoke({
    'topic' : 'black hole'
})

result = model.invoke(prompt1)

print("FIRST OUTPUT:")
print(result.content)


prompt2 = temp2.invoke({
    'text' : result.content
})

print("SECOND PROMPT:")
print(prompt2.to_string())

res2 = model.invoke(prompt2)


print("FINAL SUMMARY:")
print(res2.content)