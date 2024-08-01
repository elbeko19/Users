from django.contrib import admin
from .models import UsersModel

class UsersModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'username', 'password']


admin.site.register(UsersModel, UsersModelAdmin)

