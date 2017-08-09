import logging
from django.utils.encoding import smart_str
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


from tools.models import Picture

from utils.utils import *

logger = logging.getLogger(__name__)


# Create your views here.
# HTML views
@login_required
def tools_index(request):
    return render(request, 'tools/tools_index.html', {'title': 'tools'})


@login_required
def picture_index(request):
    pictures = Picture.objects.all().filter(
        owner=request.user).all().order_by('-id')
    paginator = Paginator(pictures, 16)
    page = request.GET.get('page')
    try:
        picture_list = paginator.page(page)
    except PageNotAnInteger:
        picture_list = paginator.page(1)
    except EmptyPage:
        picture_list = paginator.paginator(paginator.num_pages)
    return render(request, 'tools/picture_index.html',
                  {'title': 'tools',
                   'picture_list': picture_list})


@login_required
def picture_new(request):
    if request.method == 'GET':
        return render(request, 'tools/picture_new.html', {'title': 'app'})
    else:
        for key, value in request.FILES.items():
            picture = Picture(pic=value, owner=request.user)
            picture.save()
            picture.refresh_from_db()
            picture.name = picture.pic.url.split('/')[4]
            picture.desc = picture.pic.url.split('/')[4]
            picture.save()
            picture.refresh_from_db()

        markdown_link, view_link, download_link = get_all_picture_url(
            picture, request.META['HTTP_HOST'])
        response = JsonResponse({
            'msg': '上传成功！',
            'markdown_link': markdown_link,
            'view_link': view_link,
            'download_link': download_link
        })
        return response


def picture_view(request, name):
    try:
        picture = Picture.objects.filter(name=name)[0]
    except ObjectDoesNotExist as e:
        picture = None
        logger.error(' ============ ObjectDoesNotExist ============')
        logger.error(e)
        raise Http404
    if picture:
        markdown_link, view_link, download_link = get_all_picture_url(
            picture, request.META['HTTP_HOST'])
        return render(request, 'tools/picture_view.html', {
            'title': 'tools',
            'picture': picture,
            'markdown_link': markdown_link,
            'view_link': view_link,
            'download_link': download_link,
        })
    else:
        return Http404


def picture_download(request, name):
    try:
        picture = Picture.objects.filter(name=name)[0]
    except ObjectDoesNotExist as e:
        picture = None
        logger.error(' ============ ObjectDoesNotExist ============')
        logger.error(e)
        raise Http404
    if picture:
        protocal = "http://"
        # protocal = "https://"
        site_domain = protocal + request.META['HTTP_HOST']
        download_link = site_domain + '/tools/picture/download/' + picture.name

        response = HttpResponse(
            content_type='application/force-download'
        )  # mimetype is replaced by content_type for django 1.7
        response[
            'Content-Disposition'] = 'attachment; filename=%s' % smart_str(
                picture.name)
        response['X-Sendfile'] = smart_str(download_link)
        # It's usually a good idea to set the 'Content-Length' header too.
        # You can also set any other required headers: Cache-Control, etc.
        return response


@login_required
def url_shorten_index(request):
    return render(request, 'tools/url_shorten_index.html', {'title': 'tools'})


@login_required
def github_star_index(request):
    return render(request, 'tools/github_star_index.html',
                  {'title': 'atoolspps'})
