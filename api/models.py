from pydantic import BaseModel
from typing import Dict, Any

class AppRequest(BaseModel):
    description: str
    project_type: str = "Web Application"
    features: list[str] = ["Authentication"]

class AppResponse(BaseModel):
    structure: Dict[str, Any]
    files: Dict[str, str]
    documentation: str
    test_results: Dict[str, Any]
