from django.db import models
from django.utils import timezone


class Transaction(models.Model):
    household = models.ForeignKey('household.Household')
    description = models.CharField(max_length=100)
    datetime = models.DateTimeField(default=timezone.now)
    participants = models.ManyToManyField('household.Inhabitant', through='TransactionParticipant')


class TransactionParticipant(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction = models.ForeignKey('Transaction')
    inhabitant = models.ForeignKey('household.Inhabitant')
