from django.conf import settings


def get_all_picture_url(picture, http_host):
    if settings.DEBUG is True:
        protocal = 'http'
    else:
        protocal = 'https'

    site_domain = protocal + http_host
    markdown_link = "![" + picture.name + "](" + site_domain + picture.pic.url + ")"
    view_link = site_domain + '/tools/picture/view/' + picture.name + '/'
    download_link = site_domain + '/tools/picture/download/' + picture.name + '/'

    return markdown_link, view_link, download_link
