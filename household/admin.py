from django.contrib import admin
from django.contrib.admin import ModelAdmin

from household.models import Household, Resident


@admin.register(Household)
class HouseholdAdmin(ModelAdmin):
    list_display = ('__str__', 'get_full_address')


@admin.register(Resident)
class ResidentAdmin(ModelAdmin):
    list_display = ('__str__', 'household')
