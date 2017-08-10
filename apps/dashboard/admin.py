from django.contrib import admin
from apps.dashboard.models import Inventory


# Register your models here.
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ip', 'regions', 'create_time', 'update_time', 'tag_list')
    search_fields = ('name', 'ip', 'regions', 'create_time', 'update_time', 'tag_list')
    list_filter = ('create_time',)
    date_hierarchy = 'create_time'


    def get_queryset(self, request):
        return super(InventoryAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


admin.site.register(Inventory, InventoryAdmin)
