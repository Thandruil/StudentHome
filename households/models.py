from django.contrib.auth.models import User
from django.db import models


class Household(models.Model):
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    postal = models.CharField(max_length=6)
    city = models.CharField(max_length=50)

    token = models.CharField(max_length=10, unique=True)

    def get_full_address(self):
        return '%s %s, %s' % (self.street, self.number, self.city)
    get_full_address.short_description = 'Address'

    def __str__(self):
        return self.name


class Inhabitant(models.Model):
    user = models.OneToOneField(User)
    household = models.ForeignKey('Household')
    room = models.IntegerField()

    def __str__(self):
        return '%s' % (self.user.get_full_name())
