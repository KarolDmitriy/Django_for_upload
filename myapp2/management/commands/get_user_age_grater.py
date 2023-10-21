from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('age', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        age = kwargs['age']
        user = User.objects.filter(age__gt=age).first()
        self.stdout.write(f'{user}')

