from django.contrib import admin

# Register your models here.
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['id', 'name']
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class RecipesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'time_create', 'time_update', 'is_published']
    list_display_links = ['id', 'title']
    search_fields = ('title', 'recipe')
    list_editable = ('is_published',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Recipes, RecipesAdmin)
admin.site.register(Category, CategoryAdmin)