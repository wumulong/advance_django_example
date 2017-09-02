from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from .models import User


# Register your models here.
class UserAdmin(AuthUserAdmin):
    list_display = ('id', 'email', 'username', 'nickname', 'is_superuser',
                    'is_staff', 'is_active')
    search_fields = ('email', 'username', 'nickname')

    fieldsets = AuthUserAdmin.fieldsets + ((None, {
        'fields': ('nickname', 'bio', 'url', 'location', 'avatar')
    }), )


admin.site.register(User, UserAdmin)
