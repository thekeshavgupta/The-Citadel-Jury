from Agents.agent import Agent
from OutputParsers.jury_output import JuryOutput
from Prompts.jury_prompt import JuryPrompt
from langchain_core.output_parsers import PydanticOutputParser
class AgentJury(Agent):
    def __init__(self, model_name, temperature, model_provider):
        super().__init__(model_name, temperature, model_provider)
        self.agent = super().initialiseAgent()
    def get_verdict(self, debateHistory: list[str] = None, userClaim: str = ""):
        parser = PydanticOutputParser(pydantic_object=JuryOutput)
        # structured_output = self.agent.with_structured_output(JuryOutput)
        prompt = JuryPrompt(debateHistory, userClaim, parser)
        prompt = prompt.generatePrompt()
        result = self.agent.invoke(prompt)
        return parser.parse(result.content)
    
        