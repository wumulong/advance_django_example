from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe


register = template.Library()  # 自定义filter时必须加上

@register.filter(is_safe=True)
@stringfilter
def custom_tags(value):
    return ', '.join([tag.name for tag in value.tags.all()])
