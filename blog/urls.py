from django.urls import path
from .views import home_page, posts_page

urlpatterns = [
    path('', home_page),
    path('posts/', posts_page),
]