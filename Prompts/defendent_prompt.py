from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

class DefendentPrompt:
    def __init__(self, messageHistory, userclaim, parser:PydanticOutputParser):
        self.history = messageHistory
        self.userClaim = userclaim
        self.parser = parser
    def generatePrompt(self):
        template = PromptTemplate(
            template="""
             You are a Defendent Lawyer and you are given a claim from a user i.e. {userclaim} and your responsibility is to analyse the user claim and list out the different findings on why you think that the user claim is valid. Below is the history of the debate happened so far and what points have been put forwarded by the prosecutor against the user claim and how you responded back to those.
            {debateHistory}.
            \n
            {format_instruction}
            """,
            input_variables=['userclaim', 'debateHistory'],
            validate_template=True,
            partial_variables=[{
                'format_instruction': self.parser.get_format_instructions()
            }]
        )
        
        return template.invoke({
            "userclaim": self.userClaim,
            "debateHistory": self.history
        })