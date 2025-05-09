from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('username',)
    ordering = ('-date_joined',)  
    list_display = ('username', 'course')  

admin.site.register(User, UserAdminConfig)
