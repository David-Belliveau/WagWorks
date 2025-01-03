from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Pet

# @admin.register(Pet)
# class PetAdmin(admin.ModelAdmin):
#     list_display = ('pet_name', 'breed', 'email', 'birthday')  # Field names to display
