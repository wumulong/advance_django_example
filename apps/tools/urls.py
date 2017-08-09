from django.conf.urls import url
from tools import views

app_name = 'tools'
urlpatterns = [
    # html view
    url(r'^$', views.tools_index, name='tools_index'),
    url(r'^picture/$', views.picture_index, name='picture_index'),
    url(r'^picture/new/$', views.picture_new, name='picture_new'),
    url(r'^picture/upload/$', views.picture_new, name='picture_new'),
    url(r'^picture/view/(?P<name>([-\w]+\.(?:jpg|gif|png|jpeg)))/$', views.picture_view, name='picture_view'),
    url(r'^picture/download/(?P<name>([-\w]+\.(?:jpg|gif|png|jpeg)))/$',
        views.picture_download,
        name='picture_download'),
    url(r'^url_shorten/$', views.url_shorten_index, name='url_shorten_index'),
    url(r'^github_star/$', views.github_star_index, name='github_star_index'),
]
