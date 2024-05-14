from typing import Any, Literal
from uuid import UUID, uuid4

from pydantic import BaseModel

from src.application.services.mediator import Dispatch
from src.application.services.service_email import SendEmailResetPasswordHandler
from src.infra.repository.user_repository import UserRepository

class Input(BaseModel):
    email: str
    password: UUID = uuid4().hex
    events: Literal['pre-register', 'new-user', 'reset-password'] = 'reset-password'

class OutputSuccess(BaseModel):
    id: str | UUID
    events: Any

class OutputError(BaseModel):
    error: str

class ResetPassword:
    def __init__(self, repo: UserRepository) -> None:
        self._repo = repo
    
    @Dispatch(SendEmailResetPasswordHandler())
    def execute(self, input: Input) -> OutputSuccess:
        success, msg = self._repo.reset_password(email=input.email, password=input.password)
        if success:
            return OutputSuccess(id=msg, events=["reset-password"])
        return OutputError(error=msg)