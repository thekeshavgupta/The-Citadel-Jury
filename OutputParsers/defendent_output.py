from typing import Optional
from pydantic import Field, BaseModel

class DefendentOutput(BaseModel):
    findings:Optional[list[str]] = Field("Contains the findings on why the defendent agent thinks that it is a valid user claim")