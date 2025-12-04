from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

class JuryPrompt:
    def __init__(self, messageHistory, userclaim, parser: PydanticOutputParser):
        self.history = messageHistory
        self.userClaim = userclaim
        self.parser = parser
    def generatePrompt(self):
        template = PromptTemplate(
            template="""
             You are a Jury and you are given a claim from a user i.e. {userclaim} and your responsibility is to analyse the findings from both prosecutor agent as well as defendent agent thoroughly from a given findings from both parties which is listed below
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