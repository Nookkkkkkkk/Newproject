from django.contrib import admin

from accounts.models import Accounts

# Register your models here.
@admin.register(Accounts)
class RegisterAccountAdmin(admin.ModelAdmin):
    pass