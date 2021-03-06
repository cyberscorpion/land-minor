from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User

from django.contrib.auth.models import Group

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name','is_staff',)
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password','username')}),
        ('Personal info', {'fields': ('name',
                                      'account_address',
                                      'budget',
                                    )}),
        ('Permissions', {'fields': ('is_staff',
                                    'is_active',
                                   )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    list_display = ('name','username','account_address')

admin.site.register(User, UserAdmin)
