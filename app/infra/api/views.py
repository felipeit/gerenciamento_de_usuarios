from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework.permissions import IsAuthenticated

from app.application.create_user_usecase import CreateUser, Input
from app.application.delete_user_usecase import DeleteUser
from app.application.update_user_usecase import UpdateUser
from app.infra.api.serializers import UserSerializer
from app.infra.orm.models import User


class UserViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


    def create(self, request, *args, **kwargs) -> Response:
        input  = Input()
        usecase = CreateUser(input)
        return Response({"user": usecase}, status=status.HTTP_201_CREATED)
    

    def update(self, request, *args, **kwargs) -> Response:
        input  = Input()
        usecase = UpdateUser(input)
        return Response({"user": usecase})
    
    def destroy(self, request, *args, **kwargs) -> Response:
        input  = Input()
        usecase = DeleteUser(input)
        return Response({"user": usecase}, status=status.HTTP_204_NO_CONTENT)