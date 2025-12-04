from Agents.agent import Agent
from OutputParsers.prosecutor_output import ProsecutorOutput
from Prompts.prosecutor_prompt import ProsecutorPrompt
from langchain_core.output_parsers import PydanticOutputParser
class AgentProsector(Agent):
    def __init__(self, model_name, temperature, model_provider):
        super().__init__(model_name, temperature, model_provider)
        self.agent = super().initialiseAgent()
    def perform_prosecution(self, debateHistory: list[str] = None, userClaim: str = ""):
        parser = PydanticOutputParser(pydantic_object=ProsecutorOutput)
        # structured_output = self.agent.with_structured_output(ProsecutorOutput)
        prompt = ProsecutorPrompt(debateHistory, userClaim, parser)
        return self.agent.invoke(prompt.generatePrompt())
        
    
        