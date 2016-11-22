from django.contrib import admin

# Register your models here.
from django.contrib import admin

from woseba.models import Kawa

@admin.register(Kawa)
class KawaAdmin(admin.ModelAdmin):
    pass