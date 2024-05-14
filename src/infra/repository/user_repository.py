from typing import Any
from uuid import UUID, uuid1

from sqlalchemy.orm import sessionmaker
from src.infra.orm.sqlalchemy.user_db import User
from src.infra.orm.sqlalchemy.conn_sqlachemy import engine



class UserRepository:
    def __init__(self, db: User = User()) -> None:
        self._db = db
        self._session = sessionmaker(bind=engine)
    
    def create_user(self, input: Any) -> None:
        new_user  = self._db(
            id = input.id,
            first_name = input.first_name,
            last_name = input.last_name,
            email =  input.email,
            cpf = input.cpf,
            cnpj = input.cnpj,
            address = input.address,
            phone_number = input.phone_number,
            active = True,
            age = input.age,
            image = input.image,
            password = input.password,
        )
        self._session.add(new_user)
        self._session.commit()

    def update_user(self, id: UUID, user: Any) -> None:
        try:
            user = self._db(
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
                image = user.image
            )
            self._session.add(user)
            self._session.commit()
        except Exception:
            raise Exception("Model instance doesn't exist")
        
    def delete_user(self, id: UUID) -> None:
        try:
            self._session.query(User).filter(User.id == id).delete()
        except self._db.DoesNotExist:
            raise Exception("Model instance doesn't exist")
        
    def reset_password(self, email: str, password: UUID) -> tuple[bool, str]:
        success = False
        msg = ""
        try:
            user = self._session.query(User).filter(User.email == email).one_or_none()
            if user is None:
                raise ValueError("Usuário não cadastrado no sistema.")
            user.password = password
            self._session.commit()
            success = True
            msg = "Um email foi enviado com a nova senha."
        except ValueError as e:
            msg = str(e)
        except Exception as e:
            msg = "Ocorreu um erro ao tentar redefinir a senha."
        return success, msg
    
    def get_user_for_email(self, email: str) -> Any:
        try:
            return self._db.objects.get(email=email)
        except self._db.DoesNotExist:
            return None
    
    def pre_create_user(self, input: Any) -> Any:
        try:
            self._db(
                id=input.id, 
                email=input.email,
                password=input.password
            )
        except Exception as err:
            return f"Errors: {err}"