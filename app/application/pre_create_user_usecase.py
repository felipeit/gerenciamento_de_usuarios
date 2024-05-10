
from typing import Literal
from uuid import UUID, uuid4
from pydantic import BaseModel

from app.infra.repository.user_repository import UserRepository




class Input(BaseModel):
    id: UUID = uuid4()
    email: str
    password: str
    events: Literal['pre-register', 'new-user', 'reset-password'] = 'pre-register'

class OutputSuccess(BaseModel):
    id: UUID

class OutputError(BaseModel):
    errors: str


class PreCreateUser:
    def __init__(self, repo: UserRepository = UserRepository()) -> None:
        self._repo = repo
    
    def execute(self, input: Input) -> OutputSuccess| OutputError:
        output = self._repo.pre_create_user(input=input)
        if not output:
            return OutputSuccess(id=input.id)
        return OutputError(errors=output)