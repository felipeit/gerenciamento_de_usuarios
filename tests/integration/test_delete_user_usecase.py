from uuid import uuid4

import pytest
from src.application.create_user_usecase import CreateUser, Input
from src.application.delete_user_usecase import DeleteUser
from src.infra.repository.user_repository import UserRepository


def test_delete_a_user() -> None:
    repository = UserRepository()
    sut1 = CreateUser(repo=repository)
    sut2 = DeleteUser(repo=repository)
    input = Input(
        first_name="teste3",
        last_name="tests",
        email="yetine4743@facais.com",
        cnpj="36.667.126/0001-61",
        address="St. M-Norte QNM 34 LOJA 219",
        phone_number="1140046446",
        age=30
        )
    uuid_user = sut1.execute(input)
    output = sut2.execute(uuid_user.id)
    assert output.id
    
def test_try_delete_a_user_with_incorrect_uuid() -> None:
    repository = UserRepository()
    sut = DeleteUser(repo=repository)
    with pytest.raises(Exception):
        sut.execute(uuid4())
