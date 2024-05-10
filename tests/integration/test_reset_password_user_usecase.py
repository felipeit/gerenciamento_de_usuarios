from uuid import UUID
import pytest
from app.application.create_user_usecase import CreateUser, Input
from app.application.reset_password_user_usecase import ResetPassword, Input as InputUsername
from app.infra.repository.user_repository import UserRepository


@pytest.mark.django_db(transaction=False)
def test_reset_password_user_usecase_with_success() -> None:
    repository = UserRepository()
    sut1 = CreateUser(repo=repository)
    input_create = Input(
        first_name="teste1",
        last_name="tests",
        email="yetine4743@facais.com",
        cnpj="36.667.126/0001-61",
        address="St. M-Norte QNM 34 LOJA 219",
        phone_number="1140046446",
        age=30
        )
    sut1.execute(input_create)
    
    sut2 = ResetPassword(repo=repository)
    input_resetpsswd = InputUsername(email=input_create.email)
    output = sut2.execute(input=input_resetpsswd)
    assert output.id
