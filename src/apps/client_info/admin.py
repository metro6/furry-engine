from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(ExtTariff)
class ExtTariffAdmin(admin.ModelAdmin):
    pass


@admin.register(ExtUser)
class ExtUserAdmin(admin.ModelAdmin):
    pass


@admin.register(ClientInfo)
class ClientAdmin(admin.ModelAdmin):
    pass