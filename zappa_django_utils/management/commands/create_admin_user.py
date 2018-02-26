from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

import random
import string


class Command(BaseCommand):
    help = 'Creates a default "admin" user'

    def add_arguments(self, parser):
        parser.add_argument('arguments', nargs='*')

    def handle(self, *args, **options):
        # see: https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#referencing-the-user-model
        User = get_user_model()

        self.stdout.write(self.style.SUCCESS('Creating new admin user...'))

        # if the command args are given -> try to create user with given args
        if options['arguments']:
            try:
                User.objects.create_superuser(*options['arguments'])
                self.stdout.write(self.style.SUCCESS('Created user with given params'))
            except Exception as e:
                self.stdout.write(str(e))

        # or create default admin user
        else:
            pw = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
            User.objects.create_superuser('admin', 'admin@admin.com', pw)
            self.stdout.write(self.style.SUCCESS('Created user "admin", email: "admin@admin.com", password: ' + pw))
            self.stdout.write(self.style.SUCCESS('Log in and change this password immediately!'))
