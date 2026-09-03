import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Ensure a superuser exists with the password from DJANGO_SUPERUSER_PASSWORD'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', '')

        if not password:
            self.stderr.write('DJANGO_SUPERUSER_PASSWORD is not set, skipping')
            return

        user, created = User.objects.get_or_create(
            username=username,
            defaults={'email': email},
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)
        user.save()

        action = 'created' if created else 'password updated'
        self.stdout.write(f'Superuser {username} {action}')
