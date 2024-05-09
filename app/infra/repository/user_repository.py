from typing import Any, Callable
from uuid import UUID, uuid1

from app.infra.orm.models import User


class UserRepository:
    def __init__(self, db: Callable = User) -> None:
        self._db = db
    
    def create_user(self, user: Any) -> None:
        user = self._db.objects.create(
            id = user.id,
            first_name = user.first_name,
            last_name = user.last_name,
            email =  user.email,
            cpf = user.cpf,
            cnpj = user.cnpj,
            address = user.address,
            phone_number = user.phone_number,
            active = True,
            age = user.age,
            username = f"{user.first_name}.{user.last_name}",

        )
        user.set_password(uuid1().hex)
        user.save()

    def update_user(self, id: UUID, user: Any) -> None:
        try:
            self._db.objects.update(
                id = user.id,
                first_name = user.first_name,
                last_name = user.last_name,
                email =  user.email,
                cpf = user.cpf,
                cnpj = user.cnpj,
                address = user.address,
                phone_number = user.phone_number,
                active = user.active,
                age = user.age,
                username = f"{user.first_name}.{user.last_name}",
            )
        except self._db.DoesNotExist:
            raise Exception("Model instance doesn't exist")
        
    def delete_user(self, id: UUID) -> None:
        try:
            self._db.objects.get(id=id).delete()
        except self._db.DoesNotExist:
            raise Exception("Model instance doesn't exist")