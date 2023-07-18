from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .forms import *
from .models import *
from .utils import *


class MainPage(DataMixin, ListView):
    model = Recipes
    template_name = 'recipes/main.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipes.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(c_def.items()) + list(context.items()))


class Search(DataMixin, ListView):
    model = Recipes
    template_name = 'recipes/main.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        search_query = self.request.GET.get('q', '')
        if search_query:
            return Recipes.objects.filter(Q(title__icontains=search_query, is_published=True) | Q(recipe__icontains=search_query, is_published=True))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = f'q={self.request.GET.get("q")}&'
        c_def = self.get_user_context()
        return dict(list(c_def.items()) + list(context.items()))


class ShowCategory(DataMixin, ListView):
    model = Recipes
    template_name = 'recipes/main.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipes.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = Category.objects.get(slug=self.kwargs['cat_slug'])
        context['cat_selected'] = cat.slug
        c_def = self.get_user_context()
        return dict(list(c_def.items()) + list(context.items()))


class AddRecipe(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'recipes/addpage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(c_def.items()) + list(context.items()))


class ShowRecipe(DataMixin, DetailView):
    model = Recipes
    template_name = 'recipes/recipe.html'
    context_object_name = 'recipe'
    slug_url_kwarg = 'rec_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(c_def.items()) + list(context.items()))


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'recipes/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'recipes/authorization.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')




