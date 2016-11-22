from django.contrib import admin

# Register your models here.
from jacobs.models import Coffee


@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    pass