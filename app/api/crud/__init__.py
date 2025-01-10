from pydantic import BaseModel

from typing import Any

class Result(BaseModel):
    success: bool
    code: int
    data: Any = None
    error: str = None