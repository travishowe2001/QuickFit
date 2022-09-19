from django.contrib import admin
from members.models import Account

# Register your models here.
from .models import Health_Data
admin.site.register(Health_Data)

admin.site.register(Account)