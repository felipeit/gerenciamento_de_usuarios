from django.forms import ValidationError
from app.domain.user import User


async def test_create_instance_valid_data() -> None:
    user, errors = User.create_instance(
        first_name='John',
        last_name='Doe',
        email='john@example.com',
        cpf='123.456.789-09',
        cnpj='11.222.333/0001-81',
        address='123 Main St',
        phone_number='123-456-7890',
        age=25,
        password=''
    )
    assert user is not None
    assert errors == []
    assert user.first_name == 'John'
    assert user.last_name == 'Doe'
    assert user.email == 'john@example.com'
    assert user.cpf == '12345678909'
    assert user.cnpj == '11222333000181'
    assert user.address == '123 Main St'
    assert user.phone_number == '123-456-7890'
    assert user.age == 25
    assert user.active
    assert user.password == ''


async def test_create_instance_invalid_age() -> None:
    user, errors = User.create_instance(
        first_name='John',
        last_name='Doe',
        email='john@example.com',
        cpf='123.456.789-09',
        cnpj='11.222.333/0001-81',
        address='123 Main St',
        phone_number='123-456-7890',
        age=15,
        password=''
    )
    assert errors
    assert all(isinstance(error, ValidationError) for error in errors)

async def test_create_instance_invalid_cpf() -> None:
    user, errors = User.create_instance(
        first_name='John',
        last_name='Doe',
        email='john@example.com',
        cpf='123.456.789-00',
        cnpj='11.222.333/0001-81',
        address='123 Main St',
        phone_number='123-456-7890',
        age=25,
        password=''
    )
    assert errors
    assert all(isinstance(error, ValidationError) for error in errors)

async def test_create_instance_invalid_cnpj() -> None:
    user, errors = User.create_instance(
        first_name='John',
        last_name='Doe',
        email='john@example.com',
        cpf='123.456.789-09',
        cnpj='11.222.333/0001-82',
        address='123 Main St',
        phone_number='123-456-7890',
        age=25,
        password=''
    )
    assert errors
    assert all(isinstance(error, ValidationError) for error in errors)

async def test_create_instance_invalid_email() -> None:
    user, errors = User.create_instance(
        first_name='John',
        last_name='Doe',
        email='johnexample.com',
        cpf='123.456.789-09',
        cnpj='11.222.333/0001-81',
        address='123 Main St',
        phone_number='123-456-7890',
        age=25,
        password=''
    )
    assert errors
    assert all(isinstance(error, ValidationError) for error in errors)
