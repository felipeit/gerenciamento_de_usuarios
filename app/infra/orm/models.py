from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    active = models.BooleanField(default=False)
    age = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.first_name} {self.last_name}"