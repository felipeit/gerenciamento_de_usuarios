from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework.permissions import IsAuthenticated

from app.application.create_user_usecase import CreateUser, Input as CreateInput
from app.application.delete_user_usecase import DeleteUser, Input as DeleteInput
from app.application.reset_password_user_usecase import ResetPassword, Input as ResetInput
from app.application.update_user_usecase import UpdateUser, Input as UpdateInput
from app.infra.api.serializers import ResetPasswordSerializer, UserSerializer
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


    def create(self, request, *args, **kwargs) -> Response:
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
    
    def destroy(self, request, *args, **kwargs) -> Response:
        repository = UserRepository()
        input  = DeleteInput(id=request.data.get('id'))
        usecase = DeleteUser(repo=repository)
        output = usecase.execute(id=input.id)
        return Response({"respose": output}, status=status.HTTP_204_NO_CONTENT)
    

class ResetPassowrdViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = ResetPasswordSerializer
    authentication_classes = []

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