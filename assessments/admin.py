from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Coop13)
class Coop13Admin(admin.ModelAdmin):
    pass
@admin.register(Coop20)
class Coop20Admin(admin.ModelAdmin):
    pass
@admin.register(Coop21)
class Coop21Admin(admin.ModelAdmin):
    pass
@admin.register(Coop11)
class Coop11Admin(admin.ModelAdmin):
    pass