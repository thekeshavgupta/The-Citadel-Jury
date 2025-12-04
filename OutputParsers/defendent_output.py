from typing import Optional, Annotated, TypedDict
from pydantic import Field, BaseModel

class DefendentOutput(BaseModel):
    findings:Optional[str] = Field(description="Contains the findings on why the defendent agent thinks that it is a valid user claim")