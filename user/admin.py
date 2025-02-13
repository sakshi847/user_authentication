from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Department, Role

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'dept', 'role', 'date_of_joining', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('dept', 'role', 'is_active')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Department)
admin.site.register(Role)

