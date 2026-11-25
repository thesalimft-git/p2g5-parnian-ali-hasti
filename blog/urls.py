from django.urls import path
from .views import home_page, posts_page

urlpatterns = [
    path('', home_page, name='home-page'),
    path('posts/', posts_page, name='posts-list-page'),
]





