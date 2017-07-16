from django.conf.urls import url
from . import views

app_name = 'user'
urlpatterns = [
    # html view
    url(r'^login/$', views.login_view, name='login'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^user/profile/$', views.profile_view, name='profile'),
    url(r'^user/profile/edit/$', views.profile_edit_view, name='profile_edit'),
    url(r'^user/profile/delete/$', views.profile_delete_view, name='profile_delete'),
    url(r'^user/password/edit/$', views.password_edit_view, name='password_edit'),
    # api view
    url(r'^api/v1/users/$', views.users, name='users'),
    url(r'^api/v1/users/(?P<pk>[0-9]+)/$', views.user_detail, name='user_detail'),
]
