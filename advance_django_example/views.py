import os
from django.shortcuts import render
from django.conf import settings


# Create your views here.
# HTML views
def index(request):
    return render(request, 'static_page/index.html', {'title': 'index'})


def apps(request):
    return render(request, 'static_page/apps.html', {'title': 'apps'})


def faq(request):
    faq_md_file = os.path.join(settings.BASE_DIR, 'docs', 'faq.md')
    with open(faq_md_file) as f:
        md = f.read()
        return render(request, 'static_page/faq.html',
                      {'title': 'faq',
                       'md': md})


def subscribe(request):
    if request.method == 'GET':
        return render(request, 'static_page/subscribe.html',
                      {'title': 'subscribe'})
    else:
        pass


def page_not_found(request):
    if request.method == 'GET':
        return render(request, 'static_page/404.html', {'title': '404'})
    else:
        pass


def server_error(request):
    if request.method == 'GET':
        return render(request, 'static_page/500.html', {'title': '500'})
    else:
        pass


def maintenance(request):
    if request.method == 'GET':
        return render(request, 'static_page/maintenance.html',
                      {'title': 'maintenance'})
    else:
        pass
