from django.contrib import admin
from .models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email',
      'is_superuser', 'is_staff', 'is_active',
      'nickname')
    search_fields = (
        'username', 'email', 'nickname', 'location')


admin.site.register(User, UserAdmin)
