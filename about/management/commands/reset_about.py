from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Resetea el historial de migraciones y elimina la tabla about_about'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM django_migrations WHERE app = 'about';")
            cursor.execute("DROP TABLE IF EXISTS about_about CASCADE;")
        self.stdout.write(self.style.SUCCESS('Historial de migraciones y tabla about_about eliminados.'))