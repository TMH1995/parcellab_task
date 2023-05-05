
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from shipping.services import TemperatureService
from django.utils.timezone import utc
import datetime
from .origin import Origin

class Temperature(models.Model):
    origin= models.OneToOneField(Origin,on_delete=models.CASCADE,related_name='origin_temperature')
    degree= models.FloatField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def isMoreThanTwoHours(self):
        timeDifference= datetime.datetime.utcnow().replace(tzinfo=utc)-self.updated_at
        diff_hours = timeDifference.days*24
        return diff_hours > 2

    def __str__(self):
        return f'{self.origin} - Temperature: {self.degree}'


@receiver(signals.post_save, sender=Origin)
def password_change_signal(sender, instance, **kwargs):
    temperature,created=Temperature.objects.get_or_create(origin=instance)
    if created:
        temperature.degree=TemperatureService().fetchTemperature(city=temperature.origin.city,zipCode=temperature.origin.zipCode)
        temperature.save()