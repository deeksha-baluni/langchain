from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

#  chat template
chat_template = ChatPromptTemplate([
    ('system', 'You ae a helpful cutomer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

# load chat history
chat_history = []

with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())

print(chat_history)

#  create prompt
prompt = chat_template.invoke({'chat_history': chat_history, 'query':'where is my refund' })

print(prompt)