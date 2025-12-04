from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()


class Agent:
    def __init__(self, model_name: str, temperature: float, model_provider: str):
        self.model_name = model_name
        self.temperature = temperature
        self.model_provider = model_provider
        
        
    def initialiseAgent(self) -> ChatGroq:
        # print(f"{self.model_name} --- {self.model_provider} ---- {self.temperature}")
        if self.model_provider == "groq":
            return ChatGroq(
                model_name=self.model_name,
                temperature= self.temperature
            )
        else:
            raise NotImplementedError("Model provider not supported yet.")