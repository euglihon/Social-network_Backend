from django.contrib import admin
from .models import Profile


# регистрация класса в админке
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'data_of_birth', 'photo']