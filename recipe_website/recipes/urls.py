from django.urls import path

from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('add-page/', add_page, name='add-page'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('recipe/<slug:rec_slug>/', show_recipe, name='show_recipe'),
    path('category/<slug:cat_slug>/', show_category, name='show_category'),
]