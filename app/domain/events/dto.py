from typing import Any

from pydantic import BaseModel


class GenericEvent(BaseModel):
    key: str
    data: Any