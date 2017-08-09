from django.conf.urls import url
from . import views

app_name = 'dashboard'
urlpatterns = [
    # html view
    url(r'^dashboard/$', views.inventory_index, name='inventory_index'),
    url(r'^inventory/$', views.inventory_index, name='inventory_index'),
    url(r'^inventory/new/$', views.inventory_new, name='inventory_new'),
    url(r'^inventory/delete/(?P<pk>[0-9]+)/$', views.inventory_delete, name='inventory_delete'),
    url(r'^inventory/(?P<pk>[0-9]+)/$', views.inventory_edit, name='inventory_edit'),
    url(r'^inventory/tag/(?P<tag>\w+)/$', views.inventory_tag, name='inventory_tag'),
]
