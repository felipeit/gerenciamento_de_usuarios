from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from app.application.pre_create_user_usecase import PreCreateUser, Input as PreCreateInput
from app.application.create_user_usecase import CreateUser, Input as CreateInput
from app.application.delete_user_usecase import DeleteUser, Input as DeleteInput
from app.application.reset_password_user_usecase import ResetPassword, Input as ResetInput
from app.application.update_user_usecase import UpdateUser, Input as UpdateInput
from app.infra.api.serializers import CreateUserSerializer, DeleteUserSerializer, PreCreateUserSerializer, ResetPasswordSerializer, UpdateUserSerializer, UserSerializer
from app.models import User
from app.infra.repository.user_repository import UserRepository


class UserViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post', 'delete', 'put']

    @extend_schema(
        request=CreateUserSerializer,
        responses={201: None}  
    )
    def create(self, request, *args, **kwargs) -> Response:
        """
        Create a new user all datas.
        responses:
          201:
            description: User created successfully.
          400:
            description: Bad request. Invalid input data.
        """
        repository = UserRepository()
        input = CreateInput(
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name'),
            email=request.data.get('email'),
            cpf=request.data.get('cpf'),
            cnpj=request.data.get('cnpj'),
            address=request.data.get('address'),
            phone_number=request.data.get('phone_number'),
            age=request.data.get('age')
        )
        usecase = CreateUser(repo=repository)
        output = usecase.execute(input=input)
        return Response({"respose": output}, status=status.HTTP_201_CREATED)
    
    @extend_schema(
        request=UpdateUserSerializer,
        responses={200: None}  
    )
    def update(self, request, *args, **kwargs) -> Response:
        repository = UserRepository()
        input  = UpdateInput(
            id=request.data.get('id'),
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name'),
            email=request.data.get('email'),
            cpf=request.data.get('cpf'),
            cnpj=request.data.get('cnpj'),
            address=request.data.get('address'),
            phone_number=request.data.get('phone_number'),
            age=request.data.get('age'),
            active=request.data.get('active')
        )
        usecase = UpdateUser(repo=repository)
        output = usecase.execute(input=input)
        return Response({"respose": output})
    
    @extend_schema(
        request=DeleteUserSerializer,
        responses={204: None}  
    )
    def destroy(self, request, *args, **kwargs) -> Response:
        repository = UserRepository()
        input  = DeleteInput(id=request.data.get('id'))
        usecase = DeleteUser(repo=repository)
        output = usecase.execute(id=input.id)
        return Response({"respose": output}, status=status.HTTP_204_NO_CONTENT)
    

class ResetPassowrdViewSet(mixins.CreateModelMixin, GenericViewSet):
    authentication_classes = []
    
    @extend_schema(
        request=ResetPasswordSerializer,
        responses={200: None}  
    )
    def create(self, request, *args, **kwargs) -> Response:
        repository = UserRepository()
        input  = ResetInput(
            email=request.data.get('email')
        )
        usecase = ResetPassword(repo=repository)
        output = usecase.execute(input=input)
        if output:
            return Response({"respose": output})
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    

class PreRegisterViewSet(mixins.CreateModelMixin, GenericViewSet):
    authentication_classes = []

    @extend_schema(
        request=PreCreateUserSerializer,
        responses={200: None}  
    )
    def create(self, request, *args, **kwargs) -> Response:
        repository = UserRepository()
        input  = PreCreateInput(
            email=request.data.get('email'),
            password=request.data.get('password')
        )
        usecase = PreCreateUser(repo=repository)
        output = usecase.execute(input=input)
        return Response({"respose": output})
        