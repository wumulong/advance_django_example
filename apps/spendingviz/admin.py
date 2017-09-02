from django.contrib import admin
from .models import Entry


# Register your models here.
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cpi_index', 'cpi_text', 'amount', 'note',
                    'tag_list', 'created_at', 'updated_at')
    search_fields = ('cpi_index', 'cpi_text', 'note', 'tags__name')

    def get_queryset(self, request):
        return super(EntryAdmin,
                     self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


admin.site.register(Entry, EntryAdmin)
