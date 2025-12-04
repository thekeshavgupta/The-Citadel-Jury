from typing import Optional
from pydantic import Field, BaseModel
class JuryOutput(BaseModel):
    confidentOfMotion: float = Field("Based upon the arguments presented from prosecutor and defendent, calculate the confidence percentage in terms of float value between 0 and 1 on how much confident the jury is that the discussion should be carried forward.")
    finalThoughts: str = Field("Based upon the arguments presented from prosecutor and defendent, give the final thoughts of the jury on the users claim.")
    verdict: str = Field("Tell based upon the jurys final decision whether the user claim is valid, insufficient in terms of information or invalid") 