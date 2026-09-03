import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create or reset the superuser password from env vars'

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
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        if email:
            user.email = email
        user.save()
        action = 'created' if created else 'password reset'
        self.stdout.write(f'Superuser {username} {action}')
