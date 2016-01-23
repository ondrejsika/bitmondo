from django.core.management.base import BaseCommand

from mondo.cron import cron


class Command(BaseCommand):
    help = 'Run mondo cron task defined in mondo/cron.py'

    def handle(self, *args, **options):
        cron()
