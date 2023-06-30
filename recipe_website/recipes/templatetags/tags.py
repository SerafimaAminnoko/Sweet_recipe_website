from django import template
from django.core.paginator import Paginator
from django.db.models import Q

from recipes.models import *

register = template.Library()


@register.simple_tag()
def category():
    return Category.objects.all()


@register.inclusion_tag('recipes/list_recipes.html')
def get_recipes_by_category(request, cat_slug):
    search_query = request.GET.get('search', '')

    if not cat_slug == 0:
        recipes = Recipes.objects.filter(cat__slug=cat_slug, is_published=True)
    elif search_query:
        recipes = Recipes.objects.filter(Q(title__icontains=search_query, is_published=True) | Q(recipe__icontains=search_query, is_published=True))
    else:
        recipes = Recipes.objects.filter(is_published=True,)

    paginator = Paginator(recipes, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return {'cat_selected': cat_slug, 'recipes': page_obj}


