from django.contrib import admin
from .models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'tag_list', 'publish_time', 'update_time')
    list_filter = ('author__username',)
    search_fields = ('title', 'author__username')

    def get_queryset(self, request):
        return super(ArticleAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())



admin.site.register(Article, ArticleAdmin)
