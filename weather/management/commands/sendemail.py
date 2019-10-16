from django.core.management.base import BaseCommand, CommandError
from weather.models import User
from weather.weather import WeatherData
from weather.email_service import sendEmail

class Command(BaseCommand):
    help = 'Sends email to users'

    def handle(self, *args, **options):
        wd = WeatherData()
        queryset = User.objects.all()
        for user in queryset:
            lat = user.location.lat
            lon = user.location.lon
            weather = wd.getWeather((lat, lon))
            try:
                sendEmail(user.location, weather, user.email)
                self.stdout.write(self.style.SUCCESS('Successfully sent email to: {}'.format(user.email)))
            except:
                self.stdout.write(self.style.ERROR('Failed to send email to: {}'.format(user.email)))
