from django.contrib import admin
from tools.models import Picture


# Register your models here.
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc', 'create_time', 'pic', 'owner')
    search_fields = ('id', 'name', 'desc', 'create_time', 'pic', 'owner')
    list_filter = ('create_time',)
    date_hierarchy = 'create_time'


admin.site.register(Picture, PictureAdmin)
