import sys
from Agents.agent_jury import AgentJury
from Agents.agent_defendent import AgentDefender
from Agents.agent_prosecutor import AgentProsector


def main(userClaim):
    # initialise the LLM which prosecutes the user claim
    agent_prosecutor = AgentProsector("llama-3.1-8b-instant", 0.8, "groq")
    
    # initialise the LLM which defends the user claim
    agent_defendent = AgentDefender("llama-3.3-70b-versatile", 0.8, "groq")
    
    # intialise the LLM which as a  jury, collects the findings and then gives the verdict
    agent_jury = AgentJury("llama-3.3-70b-versatile", 0.8, "groq")
    
    # confidenceOfMotion represents how confident the jury is that the case can be carried for further discussions
    confidenceOfMotion = 1
    round = 1
    debateHistory = []
    while(confidenceOfMotion >= 0.5):
        # agent_prosecutor makes its arguments and outputs them after analysing the whole history
        agent_prosecutor_output = agent_prosecutor.perform_prosecution(debateHistory, userClaim)
        debateHistory.append({
            "agent": "ProsecutionAgent",
            "Role": "Tell why the user claim is invalid",
            "agent_output": agent_prosecutor_output.findings
        })
        
        # Similary, agent_defendent makes its arguments and outputs them after analysing the whole history
        agent_defendent_output = agent_defendent.defend_argument(debateHistory, userClaim)
        debateHistory.append({
            "agent": "DefenderAgent",
            "Role": "Tell why the user claim is valid",
            "agent_output": agent_defendent_output.findings
        })
        
        # agent_jury analyses both the arguments and gives the verdict
        agent_jury_output = agent_jury.get_verdict(debateHistory, userClaim)
        debateHistory.append({
            "agent": "JuryAgent",
            "Role": "Analyses the findings from both the agents and tells its final verdict",
            "agent_output": agent_jury_output
        })
        
        # check whether the discussion needs to be carried forward or not.
        confidenceOfMotion = agent_jury_output.confidentOfMotion
        
        # update the round of debate
        round+=1
        print(f"***Round {round} discussion completed.... confidenceOfMotion: {confidenceOfMotion}***")
    
    print("################################")
    print(debateHistory)
    print("################################")
    
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py '<user_claim>'")
        sys.exit(1)
    
    user_claim = sys.argv[1]
    main(userClaim=user_claim)