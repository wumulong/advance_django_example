"""advance_django_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from . import views

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router = routers.DefaultRouter()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('user.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^', include('article.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^apps/', views.apps, name='apps'),
    url(r'^maintenance/', views.maintenance, name='maintenance'),
    # rest_framework urls
    url(r'^', include(router.urls)),
    url(r'^api/v1/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/api-token-auth/', obtain_jwt_token),
    url(r'^api/v1/api-token-refresh/', refresh_jwt_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = views.page_not_found
handler500 = views.server_error


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
