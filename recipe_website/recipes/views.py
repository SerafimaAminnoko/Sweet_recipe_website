from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import *
from .models import *

menu = [{'title': 'Add Page', 'url_name': 'add-page'},

]


def main(request):
    context = {
        'menu': menu,
        'cat_selected': 0,
    }
    return render(request, 'recipes/main.html', context=context)


def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    context = {
        'form': form,
        'menu': menu,

    }
    return render(request, 'recipes/addpage.html', context=context)


def show_category(request, cat_slug):
    context = {
        'menu': menu,
        'title': "selection by rubric",
        'cat_selected': cat_slug
    }
    return render(request, 'recipes/main.html', context=context)


def show_recipe(request, rec_slug):
    recipe = get_object_or_404(Recipes, slug=rec_slug)
    context = {
        'recipe': recipe,
        'menu': menu,
        'title': recipe.title,
        'cat_selected': recipe.cat,
    }
    return render(request, 'recipes/recipe.html', context=context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'recipes/register.html'
    success_url = reverse_lazy('login')
    extra_context = {'menu': menu,}

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




