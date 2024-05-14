from fastapi import FastAPI
from src.infra.repository.user_repository import UserRepository
from src.application.pre_create_user_usecase import Input as PreCreateInput, PreCreateUser
from src.application.create_user_usecase import Input as CreateInput, CreateUser
from src.application.update_user_usecase import Input as UpdateInput, UpdateUser
from src.application.delete_user_usecase import Input as DeleteInput, DeleteUser
from src.application.reset_password_user_usecase import Input as ResetInput, ResetPassword
app = FastAPI()


@app.get("/")
async def get_users(input: CreateInput) -> None:
    return {"Hello": "World"}

@app.post("/")
async def pre_create_user(input: PreCreateInput) -> None:
    repository = UserRepository()
    usecase = PreCreateUser(repo=repository)
    output = usecase.execute(input)
    return output

@app.post("/create-user")
async def create_user(input: CreateInput) -> None:
    repository = UserRepository()
    usecase = CreateUser(repo_user=repository)
    output = usecase.execute(input)
    return output

@app.patch("update-user/{user_id}")
async def update_user(input: UpdateInput) -> None:
    repository = UserRepository()
    usecase = UpdateUser(repo_user=repository)
    output = usecase.execute(input)
    return output

@app.delete("delete-user/{user_id}")
async def delete_user(input: DeleteInput) -> None:
    repository = UserRepository()
    usecase = DeleteUser(repo_user=repository)
    output = usecase.execute(input)
    return output

@app.post("/reset-password")
async def reset_password(input: ResetInput) -> None:
    repository = UserRepository()
    usecase = ResetPassword(repo_user=repository)
    output = usecase.execute(input)
    return output