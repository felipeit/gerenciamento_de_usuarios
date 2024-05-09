from typing import Any, Literal
from uuid import UUID, uuid4

from pydantic import BaseModel

from app.application.services.mediator import Dispatch
from app.application.services.service_email import SendEmailResetPasswordHandler
from app.infra.repository.user_repository import UserRepository

class Input(BaseModel):
    username: str
    password: UUID = uuid4().hex

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
        success, msg = self._repo.reset_password(username=input.username, password=input.password)
        if success:
            return OutputSuccess(id=msg, events=["reset-password"])
        return OutputError(error=msg)