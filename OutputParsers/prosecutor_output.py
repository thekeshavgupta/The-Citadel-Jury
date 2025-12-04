from typing import Optional
from pydantic import BaseModel, Field

class ProsecutorOutput(BaseModel):
    findings: Optional[list[str]] = Field("Findings on why the prosecution agent thinks that it is not a valid user claim and list them out")