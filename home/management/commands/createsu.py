from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="PatrickCoakley23").exists():
            User.objects.create_superuser("PatrickCoakley23", "patrickcoakley23@gmail.com", "password")