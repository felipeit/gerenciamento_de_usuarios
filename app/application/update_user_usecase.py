from typing import Any
from uuid import UUID
from pydantic import BaseModel

from app.domain.user import User
from app.infra.repository.cat_repository import CatRepository
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
    def __init__(self, repo_user: UserRepository, repo_cat: CatRepository = CatRepository()) -> None:
        self._repo_user = repo_user
        self._repo_cat = repo_cat

    def execute(self, input: Input) -> OutputSuccess | OutputError:
        user, errors = User.update_instance(
            first_name=input.first_name, 
            last_name=input.last_name, 
            email=input.email, 
            cpf=input.cpf, 
            cnpj=input.cnpj, 
            address=input.address, 
            phone_number=input.phone_number, 
            age=input.age,
            image=self._repo_cat.get_random_pic(),
        )
        if not errors:
            self._repo_user.update_user(input.id, user)
            return OutputSuccess(id=input.id)
        return OutputError(errors=errors)