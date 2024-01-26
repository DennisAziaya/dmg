# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'workspace_id', 'first_name', 'last_name', 'is_active']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['is_active']
    fieldsets = (
        (None, {'fields': ('workspace_id', 'email', 'username', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_employee', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
