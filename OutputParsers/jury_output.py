from typing import Literal, Optional
from pydantic import Field, BaseModel
class JuryOutput(BaseModel):
    confidentOfMotion: Literal[0,1] = Field("Based upon the arguments presented from prosecutor and defendent so far, tell whether the discussion needs to be stopped now or not. Output 0 if discussion needs to be stopped else 1 if you need more information to reach final verdict")
    finalThoughts: str = Field("Based upon the arguments presented from prosecutor and defendent, give the final thoughts of the jury on the users claim.")
    verdict: str = Field("Tell based upon the jurys final decision whether the user claim is valid, insufficient in terms of information or invalid") 