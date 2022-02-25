from django.core.management.base import BaseCommand
from apps.authentication.models import User

class Command(BaseCommand):
  def handle(self, *args, **options):
        User.objects.create_superuser( "patrickcoakley23@outlook.com", "020408") # email/username and the password
