from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from accounts.models import *
from utilities.db.admin import BaseAdminMixin


@admin.register(Permission)
class PermissionAdmin(BaseAdminMixin):
    list_display = ('code', 'name', 'resource', 'created_on')
    search_fields = ('code', 'name')
    list_filter = ('resource', )


@admin.register(Role)
class RoleAdmin(BaseAdminMixin):
    list_display = ('name', 'created_on', 'modified_on')
    search_fields = ('name', )
    filter_horizontal = ('permissions', )


@admin.register(Team)
class TeamAdmin(BaseAdminMixin):
    list_filter = ('name', 'description')
    search_fields = ('name',)


@admin.register(Employee)
class EmployeeAdmin(UserAdmin, BaseAdminMixin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Details'), {'fields': ('first_name', 'last_name', 'employee_id', 'team', 'position')}),
        (_('Personal Information'), {'fields': ('email', 'phone_no')}),
        (_('Permissions'), {
            'fields': ('is_active', 'permissions', 'roles'),
        }),
        (_('Miscellaneous'), {'fields': ('created_on', 'modified_on', 'last_login', 'date_joined')}),
    )
    list_display = ('username', 'employee_id', 'first_name', 'last_name', 'team', 'position', 'is_active', 'last_login', 'date_joined')
    list_filter = ('team', 'position', 'date_joined', 'last_login')
    filter_horizontal = ('permissions', 'roles')
    readonly_fields = ('last_login', 'date_joined')
