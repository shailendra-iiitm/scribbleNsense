from pydantic import BaseModel
from typing import Dict, Any, Optional

class ImageData(BaseModel):
    image: str  # Base64 encoded image data
    dict_of_vars: Dict[str, Any] = {}  # Dictionary of variables

class CalculationResponse(BaseModel):
    expr: str
    result: str
    assign: bool = False

class APIResponse(BaseModel):
    message: str
    data: list[CalculationResponse] = []
    status: str