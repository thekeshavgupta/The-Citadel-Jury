from typing import Optional, Annotated, TypedDict
from pydantic import Field, BaseModel
class JuryOutput(BaseModel):
    confidentOfMotion: int = Field("Based upon the arguments presented from prosecutor and defendent, calculate in terms of probability hom much confident the jury is that the discussion should be carried forward.")
    finalThoughts: Optional[str] = Field("Based upon the arguments presented from prosecutor and defendent, give the final thoughts of the jury on the users claim.")
    verdict: str = Field("Tell based upon the jurys final decision whether the user claim is valid, insufficient in terms of information or invalid") 