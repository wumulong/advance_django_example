import logging
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from rest_framework.decorators import api_view
# from rest_framework.response import Response

from dashboard.models import Inventory
# from dashboard.serializers import InventorySerializer

from cryptography.fernet import Fernet

logger = logging.getLogger(__name__)


# Create your views here.
# HTML views
@login_required
def dashboard_index(request):
    return render(request, 'dashboard/dashboard_index.html',
                  {'title': 'dashboard'})


@login_required
def inventory_index(request):
    inventories = Inventory.objects.all().filter(
        owner=request.user).all().order_by('-id')
    paginator = Paginator(inventories, 10)
    page = request.GET.get('page')
    try:
        inventory_list = paginator.page(page)
    except PageNotAnInteger:
        inventory_list = paginator.page(1)
    except EmptyPage:
        inventory_list = paginator.paginator(paginator.num_pages)
    return render(request, 'dashboard/inventory_index.html',
                  {'title': 'inventory',
                   'inventory_list': inventory_list})


@login_required
def inventory_new(request):
    if request.method == 'GET':
        return render(request, 'dashboard/inventory_new.html',
                      {'title': 'inventory'})
    else:
        if request.POST.get('root_password'):
            key = Fernet.generate_key()
            f = Fernet(key)
            byte_root_password = bytes(
                request.POST.get('root_password'), encoding="utf8")
            token = f.encrypt(byte_root_password)
        inventory = Inventory(
            name=request.POST.get('name', ''),
            ip=request.POST.get('ip'),
            regions=request.POST.get('regions', ''),
            ssh_port=request.POST.get('ssh_port', ''),
            root_password_key=key,
            root_password=token,
            owner=request.user)
        try:
            inventory.full_clean()
        except ValidationError as e:
            messages.warning(request, e.messages[0])
            return HttpResponseRedirect('/inventory/')
        inventory.save()
        # inventory.refresh_from_db()
        for i in request.POST.get('tags', '').split(','):
            inventory.tags.add(i)
        messages.success(request, '新增资产成功！')
        return HttpResponseRedirect('/inventory/')


@login_required
def inventory_delete(request, pk):
    if request.method == 'DELETE':
        try:
            inventory = Inventory.objects.get(id=pk)
        except ObjectDoesNotExist as e:
            inventory = None
            logger.error(' ============ ObjectDoesNotExist ============')
            logger.error(e)
            raise Http404
        if inventory:
            inventory.delete()
            return JsonResponse({'result': 'ok'}, status=200)


@login_required
def inventory_edit(request, pk):
    try:
        inventory = Inventory.objects.get(id=pk)
    except ObjectDoesNotExist as e:
        inventory = None
        logger.error(' ============ ObjectDoesNotExist ============')
        logger.error(e)
        raise Http404
    if inventory:
        if request.method == 'GET':
            return render(request, 'dashboard/inventory_edit.html',
                          {'title': 'inventory',
                           'inventory': inventory})
        else:
            inventory.name = request.POST.get('name', '')
            inventory.ip = request.POST.get('ip')
            inventory.regions = request.POST.get('regions', '')
            inventory.save()
            inventory.tags.clear()
            for i in request.POST.get('tags', '').split(','):
                inventory.tags.add(i)
            # inventory.refresh_from_db()
            messages.success(request, '更新成功')
            return render(request, 'dashboard/inventory_edit.html',
                          {'title': 'inventory',
                           'inventory': inventory})


@login_required
def inventory_tag(request, tag):
    inventories = Inventory.objects.filter(
        tags__name__in=tag.split(' ')).distinct().order_by('-id')
    paginator = Paginator(inventories, 10)
    page = request.GET.get('page')
    try:
        inventory_list = paginator.page(page)
    except PageNotAnInteger:
        inventory_list = paginator.page(1)
    except EmptyPage:
        inventory_list = paginator.paginator(paginator.num_pages)
    return render(request, 'dashboard/inventory_index.html', {
        'title': 'inventory',
        'tag_name': tag,
        'inventory_list': inventory_list
    })
