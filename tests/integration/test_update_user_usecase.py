import pytest
from src.application.create_user_usecase import CreateUser, Input as InputOutId
from src.application.update_user_usecase import UpdateUser, Input
from src.infra.repository.user_repository import UserRepository


def test_update_user_usecase_with_data_correct() -> None:
    repository = UserRepository()
    sut1 = CreateUser(repo=repository)
    sut2 = UpdateUser(repo=repository)
    input_create = InputOutId(
        first_name="teste6",
        last_name="tests",
        email="yetine4743@facais.com",
        cpf="722.833.710-74",
        cnpj="36.667.126/0001-61",
        address="St. M-Norte QNM 34 LOJA 219",
        phone_number="1140046446",
        age=30
        )
    uuid_user = sut1.execute(input_create)

    input_update = Input(
        id=uuid_user.id,
        first_name="teste7",
        last_name="tests",
        email="yetine4743@facais.com",
        cpf="722.833.710-74",
        cnpj="36.667.126/0001-61",
        address="St. M-Norte QNM 34 LOJA 219",
        phone_number="1140046446",
        age=31,
        active=False
    )
    output = sut2.execute(input_update)
    assert output.id

    
def test_update_user_usecase_with_data_incorrect() -> None:
    repository = UserRepository()
    sut1 = CreateUser(repo=repository)
    sut2 = UpdateUser(repo=repository)
    input_create = InputOutId(
        first_name="teste4",
        last_name="tests",
        email="yetine4743@facais.com",
        cnpj="36.667.126/0001-61",
        address="St. M-Norte QNM 34 LOJA 219",
        phone_number="1140046446",
        age=30
        )
    uuid_user = sut1.execute(input_create)

    input_update = Input(
        id=uuid_user.id,
        first_name="teste5",
        last_name="tests",
        email="yetine4743#facais.com",
        cpf="722.833.710-741",
        address="St. M-Norte QNM 34 LOJA 219",
        phone_number="1140046446",
        age=17,
        active=False
    )
    output = sut2.execute(input_update)
    assert len(output.errors) == 3