from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('search', Search.as_view(), name='search'),
    path('add-page/', AddRecipe.as_view(), name='add-page'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('recipe/<slug:rec_slug>/', ShowRecipe.as_view(), name='show_recipe'),
    path('category/<slug:cat_slug>/', ShowCategory.as_view(), name='show_category'),
]