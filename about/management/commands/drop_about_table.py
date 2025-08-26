from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Drop the about_about table manually'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute('DROP TABLE IF EXISTS about_about CASCADE;')
        self.stdout.write(self.style.SUCCESS('Table about_about dropped successfully.'))