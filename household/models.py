from django.contrib.auth.models import User
from django.db import models
from django.utils.crypto import get_random_string

TOKEN_LENGTH = 8


class Household(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    postal = models.CharField(max_length=6)
    city = models.CharField(max_length=50)
    residents = models.ManyToManyField(User, through='Resident')

    token = models.CharField(max_length=TOKEN_LENGTH, blank=True, unique=True)

    def get_name(self):
        return self.name or self.get_street_address()

    def get_street_address(self):
        return '%s %s' % (self.street, self.number)

    def get_full_address(self):
        return '%s\n' \
               '%s %s' % (self.get_street_address(), self.postal, self.city)

    def generate_token(self):
        while True:
            self.token = get_random_string(length=TOKEN_LENGTH)
            if not Household.objects.filter(token=self.token):
                break

    def save(self, *args, **kwargs):
        if not self.token:
            self.generate_token()
        super(Household, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Resident(models.Model):
    user = models.ForeignKey('User')
    household = models.ForeignKey('Household')
    is_manager = models.BooleanField()

    def __str__(self):
        return '%s' % (self.user.get_full_name())
