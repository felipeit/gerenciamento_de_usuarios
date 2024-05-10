from uuid import UUID, uuid4
from django.forms import ValidationError
from validate_docbr import CPF, CNPJ

from app.domain.helpers import clean_cpf_or_cnpj


class User:
    def __init__(
            self,
            first_name: str, 
            last_name: str, 
            email: str, 
            address: str, 
            phone_number: str, 
            age: int,
            password: str,
            cnpj: str | None = None, 
            cpf: str | None = None,
    ) -> None:
        self.__id = uuid4()
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__cpf = cpf
        self.__cnpj = cnpj
        self.__address = address
        self.__phone_number = phone_number
        self.__age = age
        self.__password = password
        self.__active = True
        self.__events = ["reset-password", "new-user"]
        
    @staticmethod
    def create_instance( 
        first_name: str, 
            last_name: str, 
            email: str, 
            cpf: str, 
            cnpj: str, 
            address: str, 
            phone_number: str, 
            age: int,
            password: str
            ) -> None:
        errors = []
        if age < 18:
            errors.append(ValidationError("Idade não permitida"))
        validator_cpf = CPF()
        if cpf and not validator_cpf.validate(cpf):
            errors.append(ValidationError("CPF inválido"))
        validator_cnpj = CNPJ()
        if cnpj and not validator_cnpj.validate(cnpj):
            errors.append(ValidationError("CNPJ inválido"))
        if '@' not in email:
            errors.append(ValidationError("Email inválido"))
        new_user =  User(
            first_name=first_name, 
            last_name=last_name, 
            email=email, 
            cpf=cpf, 
            cnpj=cnpj, 
            address=address, 
            phone_number=phone_number, 
            age=age,
            password=password
        )
        if not errors:
            return new_user, errors
        return None, errors
    
    @staticmethod
    def update_instance( 
        first_name: str, 
            last_name: str, 
            email: str, 
            cpf: str, 
            cnpj: str, 
            address: str, 
            phone_number: str, 
            age: int,
            ) -> None:
        errors = []
        if age < 18:
            errors.append(ValidationError("Idade não permitida"))
        validator_cpf = CPF()
        if cpf and not validator_cpf.validate(cpf):
            errors.append(ValidationError("CPF inválido"))
        validator_cnpj = CNPJ()
        if cnpj and not validator_cnpj.validate(cnpj):
            errors.append(ValidationError("CNPJ inválido"))
        if '@' not in email:
            errors.append(ValidationError("Email inválido"))
        new_user =  User(
            first_name=first_name, 
            last_name=last_name, 
            email=email, 
            cpf=cpf, 
            cnpj=cnpj, 
            address=address, 
            phone_number=phone_number, 
            age=age,
            password="",
        )
        if not errors:
            return new_user, errors
        return None, errors
    
    @property
    def id(self) -> UUID:
        return self.__id
    
    @property
    def age(self) -> int:
        return self.__age
    
    @property
    def first_name(self) -> str:
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        return self.__last_name
    
    @property
    def full_name(self) -> str:
        return f"{self.__first_name} {self.__last_name}"

    @property
    def cpf(self) -> str:
        return clean_cpf_or_cnpj(self.__cpf)
    
    @property
    def cnpj(self) -> str:
        return clean_cpf_or_cnpj(self.__cnpj)
    
    @property
    def address(self) -> str:
        return self.__address
    
    @property
    def phone_number(self) -> str:
        return self.__phone_number

    @property
    def email(self) -> str:
        return self.__email

    @property
    def active(self) -> bool:
        return self.__active
    
    @property
    def password(self) -> str:
        return self.__password
    
    def get_events(self) -> list[str]:
        return self.__events