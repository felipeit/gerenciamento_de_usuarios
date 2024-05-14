from uuid import uuid4
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import UUIDType, EmailType, PhoneNumberType, PasswordType, URLType

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid4())
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    email = Column(EmailType(200), unique=True, nullable=False)
    cpf = Column(String(11), nullable=True)
    cnpj = Column(String(14), nullable=True)
    address = Column(String(200), nullable=True)
    phone_number = Column(PhoneNumberType(12), nullable=True)
    active = Column(Boolean, default=False)
    age = Column(Integer, nullable=True)
    image = Column(URLType, nullable=True)
    password = Column(PasswordType(200))

    def __str__(self) -> str:
        return f"{self.id} - {self.first_name} {self.last_name}"
    