from django.contrib import admin
from .models import Event, Registration


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = ['title', 'date', 'category', 'capacity']


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'event']