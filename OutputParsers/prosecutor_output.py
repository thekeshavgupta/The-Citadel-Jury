from typing import Optional, Annotated, TypedDict
from pydantic import BaseModel, Field

class ProsecutorOutput(TypedDict):
    findings: Optional[str] = Field("Findings on why the prosecution agent thinks that it is not a valid user claim")