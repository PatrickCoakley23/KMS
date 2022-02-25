from django.core.management.base import BaseCommand
from apps.authentication.models import User

class Command(BaseCommand):
  def handle(self, *args, **options):
      if not User.objects.filter(email="patrickcoakley23@outlook.com").exists(): #change email for username if you user django User model
        User.objects.create_superuser( "patrickcoakley23@outlook.com", "020408") # email/username and the password
