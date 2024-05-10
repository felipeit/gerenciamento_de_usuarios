from typing import Any
from uuid import UUID, uuid1

from app.models import User


class UserRepository:
    def __init__(self, db: User = User) -> None:
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
            #username = f"{user.first_name}.{user.last_name}",

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
            )
        except self._db.DoesNotExist:
            raise Exception("Model instance doesn't exist")
        
    def delete_user(self, id: UUID) -> None:
        try:
            self._db.objects.get(id=id).delete()
        except self._db.DoesNotExist:
            raise Exception("Model instance doesn't exist")
        
    def reset_password(self, email: str, password: UUID) -> UUID:
        success = False
        msg = ""
        try:
            user = self._db.objects.get(email=email)
            user.set_password(password)
            user.save()
            success = True
            msg = "Um email foi enviado com a nova senha."
        except self._db.DoesNotExist:
            msg = "Usuário não cadastrado no sistema."
        return success, msg
    
    def get_user_for_email(self, email: str) -> Any:
        try:
            return self._db.objects.get(email=email)
        except self._db.DoesNotExist:
            return None