from django.contrib import admin
from django.contrib.admin import ModelAdmin

from household.models import Household, Inhabitant


@admin.register(Household)
class HouseholdAdmin(ModelAdmin):
    list_display = ('name', 'get_full_address')


@admin.register(Inhabitant)
class InhabitantAdmin(ModelAdmin):
    list_display = ('__str__', 'household', 'room')
