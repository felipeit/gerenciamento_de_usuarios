import json
from uuid import uuid4
from django.core.management.base import BaseCommand
from app.models import User


class Command(BaseCommand):
    help = 'Carrega uma fixture de usuário no sistema'
        
    @classmethod
    def add_arguments(cls, parser) -> None:
        parser.add_argument(
            'initial_user', action='store_true',
            help='Measure code coverage during test execution.'
        )

    def handle(self, *args, **kwargs) -> None:
        with open('app/management/commands/fixtures/admin.json', 'r') as f:
            usuario = json.load(f)
            user = User.objects.create(
                id= uuid4(),
                first_name=usuario['first_name'],
                last_name=usuario['last_name'],
                email=usuario['email'],
                cnpj=usuario['cnpj'],
                address=usuario['address'],
                phone_number=usuario['phone_number'],
                active=True,
                age=100,
            )
            user.set_password(usuario['password'])
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Usuário {user.first_name} {user.last_name} criado com sucesso!'))
