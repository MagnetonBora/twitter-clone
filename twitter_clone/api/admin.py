from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser, Status
# Register your models here.
from .forms import AppUserChangeForm, AppUserCreationForm


class AppUserAdmin(UserAdmin):
    add_form = AppUserCreationForm
    form = AppUserChangeForm
    model = AppUser
    list_display = ('screen_name', 'name', 'email', 'is_staff', 'is_active',)
    list_filter = ('screen_name', 'name', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('screen_name', 'name', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('screen_name', 'name', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('screen_name', 'name', 'email')
    ordering = ('screen_name',)

admin.site.register(Status)
admin.site.register(AppUser, AppUserAdmin)