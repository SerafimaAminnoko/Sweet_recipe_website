from django import template
from django.core.paginator import Paginator
from django.db.models import Q

from recipes.models import *

register = template.Library()


@register.simple_tag()
def category():
    return Category.objects.all()



