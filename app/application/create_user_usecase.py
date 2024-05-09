from dataclasses import field
from typing import Any
from uuid import UUID
from pydantic import BaseModel
from app.domain.user import User
from app.infra.repository.user_repository import UserRepository


class Input(BaseModel):
    first_name: str
    last_name: str
    email: str
    cpf: str
    cnpj: str
    address: str
    phone_number: str
    age: int
        
class OutputSuccess(BaseModel):
    id: UUID

class OutputError(BaseModel):
    errors: list[Any] = field(default_factory=list)

class CreateUser:
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
            self._repo.create_user(user=user)
            return OutputSuccess(id=user.id)
        return OutputError(errors=errors)