from django.core.management.base import BaseCommand

from django.db import connections

class Command(BaseCommand):
    help = 'Tạo unique index cho trường email trong collection users.'

    def handle(self, *args, **options):
        db = connections['default'].connection
        result = db['users'].create_index([('email', 1)], unique=True)
        self.stdout.write(self.style.SUCCESS(f'Đã tạo unique index: {result}'))
