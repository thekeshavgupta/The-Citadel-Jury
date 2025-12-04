from Agents.agent import Agent
from OutputParsers.defendent_output import DefendentOutput
from Prompts.defendent_prompt import DefendentPrompt
from langchain_core.output_parsers import PydanticOutputParser
class AgentDefender(Agent):
    def __init__(self, model_name, temperature, model_provider):
        super().__init__(model_name, temperature, model_provider)
        self.agent = super().initialiseAgent()
    def defend_argument(self, debateHistory: list[str] = None, userClaim: str = ""):
        parser = PydanticOutputParser(pydantic_object=DefendentOutput)
        # structured_output = self.agent.with_structured_output(DefendentOutput)
        prompt = DefendentPrompt(debateHistory, userClaim, parser)
        return self.agent.invoke(prompt.generatePrompt())
        
    
        