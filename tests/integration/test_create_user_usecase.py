import pytest
from app.application.create_user_usecase import CreateUser, Input
from app.infra.repository.user_repository import UserRepository
from django.db import transaction


@pytest.mark.django_db(transaction=False)
def test_create_user_with_data_correct() -> None:
    repository = UserRepository()
    sut = CreateUser(repo=repository)
    input = Input(
        first_name="teste1",
        last_name="tests",
        email="yetine4743@facais.com",
        cpf="722.833.710-74",
        cnpj="36.667.126/0001-61",
        address="St. M-Norte QNM 34 LOJA 219",
        phone_number="1140046446",
        age=30
        )
    output = sut.execute(input)
    assert output.id

@pytest.mark.django_db(transaction=False)
def test_create_user_with_data_incorrect() -> None:
    repository = UserRepository()
    sut = CreateUser(repo=repository)
    input = Input(
        first_name="teste2",
        last_name="tests",
        email="yetine4743#facais.com",
        cpf="722.833.710-741",
        cnpj="36.667.126/001-61",
        address="St. M-Norte QNM 34 LOJA 219",
        phone_number="1140046446",
        age=17
        )
    output = sut.execute(input)
    assert len(output.errors) == 4