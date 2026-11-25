from django.urls import path
from .views import login_page_view, logout_page_view, register_page_view

urlpatterns = [
    path('login/', login_page_view, name='login-page'),
    path('logout/', logout_page_view, name='logout-page'),
    path('register/', register_page_view, name='register-page'),
]
