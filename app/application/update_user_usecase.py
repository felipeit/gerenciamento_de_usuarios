from typing import Any
from uuid import UUID
from pydantic import BaseModel

from app.domain.user import User
from app.infra.repository.user_repository import UserRepository


class Input(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: str
    cpf: str | None = None
    cnpj: str | None = None
    address: str
    phone_number: str
    age: int
    active: bool

class OutputSuccess(BaseModel):
    id: UUID

class OutputError(BaseModel):
    errors: list[Any]


class UpdateUser:
    def __init__(self, repo: UserRepository) -> None:
        self._repo = repo

    def execute(self, input: Input) -> OutputSuccess | OutputError:
        user, errors = User.create_instance(
            first_name=input.first_name, 
            last_name=input.last_name, 
            email=input.email, 
            cpf=input.cpf, 
            cnpj=input.cnpj, 
            address=input.address, 
            phone_number=input.phone_number, 
            age=input.age
        )
        if not errors:
            self._repo.update_user(input.id, user)
            return OutputSuccess(id=input.id)
        return OutputError(errors=errors)