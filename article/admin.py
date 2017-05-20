from django.contrib import admin
from .models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publish_time',
      'update_time')
    search_fields = (
        'title', 'author')


admin.site.register(Article, ArticleAdmin)
