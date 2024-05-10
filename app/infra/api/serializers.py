from rest_framework import serializers

from app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PreCreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class CreateUserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    cpf = serializers.CharField()
    cnpj = serializers.CharField()
    address = serializers.CharField()
    phone_number = serializers.CharField()
    age = serializers.IntegerField()

class UpdateUserSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    cpf = serializers.CharField()
    cnpj = serializers.CharField()
    address = serializers.CharField()
    phone_number = serializers.CharField()
    age = serializers.IntegerField()
    active = serializers.BooleanField()

class DeleteUserSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    
class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()