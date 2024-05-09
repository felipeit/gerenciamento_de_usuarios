from email import message
from typing import Any
from uuid import UUID
from pydantic import BaseModel

from app.domain.user import User
from app.infra.repository.user_repository import UserRepository


class Input(BaseModel):
    id: UUID | str

class OutputSuccess(BaseModel):
    id: UUID

class DeleteUser:
    def __init__(self, repo: UserRepository) -> None:
        self._repo = repo

    def execute(self, id: UUID) -> OutputSuccess:
        self._repo.delete_user(id)
        return OutputSuccess(id=id)