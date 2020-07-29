import datetime
import random
import names
from django.core.management.base import BaseCommand
from activity.models import User, Activity
from random import randrange
from datetime import timedelta, datetime
import  pytz


class Command(BaseCommand):
    help = "Save randomly generated stock record values."

    def random_timezone(self):
        """
        This function will return random timezone.
        """
        randZoneName = random.choice(pytz.all_timezones)
        return randZoneName

    def random_datetime(self):
        """
        This function will return a random datetime between two datetime 
        objects.
        """
        start = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
        end = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    def handle(self, *args, **options):
        records = []
        for _ in range(10):
            kwargs = {
                'real_name': names.get_full_name(),
                'tz': self.random_timezone(),
            }
            record = User(**kwargs)
            records.append(record)
        User.objects.bulk_create(records)

        records = []
        for _ in range(30):
            kwargs1 = {
                'start_time': self.random_datetime(),
                'end_time': self.random_datetime(),
                'userid_id' : random.randint(1, 10)
            }
            record = Activity(**kwargs1)
            records.append(record)
        Activity.objects.bulk_create(records)

        self.stdout.write(self.style.SUCCESS('Stock records saved successfully.'))