from django.contrib import admin
from .models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'nickname', 'is_superuser', 'is_staff', 'is_active')
    search_fields = ('email', 'username', 'nickname', 'location')


admin.site.register(User, UserAdmin)
