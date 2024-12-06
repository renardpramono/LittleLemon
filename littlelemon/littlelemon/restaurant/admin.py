from django.contrib import admin
from .models import Menu, Booking  # Import the models

# Register your models here.
admin.site.register(Booking)
admin.site.register(Menu)
