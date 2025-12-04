from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(
    model_name='llama-3.1-8b-instant',
    temperature=0.7
)

print(model.invoke("Capital of New Zealand is ?").content)