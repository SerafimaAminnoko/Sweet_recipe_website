from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id', 'name']


class Recipes(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField()
    recipe = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create = models.TimeField(auto_now_add=True)
    time_update = models.TimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, related_name='category')

    class Meta:
        verbose_name = 'Recipes'
        verbose_name_plural = 'Recipes'
        ordering = ['title', 'time_create']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_recipe', kwargs={'rec_slug': self.slug})
