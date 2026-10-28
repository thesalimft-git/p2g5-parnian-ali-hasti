from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home_page(request):
    return render(
        request, 
        'blog/home_page.html', 
        context = {
            'title': 'Blog | Home Page'
        }
    )

def posts_page(request):
    posts = Post.objects.filter(is_active=True)
    
    return render(
        request, 
        'blog/post_page.html', 
        context = {
            'title': 'Blog | Post List',
            'posts': posts
        }
    )