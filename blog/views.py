from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from datetime import datetime as dt


def home_page(request):
    return render(
        request, 
        'blog/home_page.html', 
        context = {
            'title': 'Blog | Home Page'
        }
    )

def posts_page(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        
        print(title, content)
        
        # validate the input
        # save into db
    else:
        posts = Post.objects.filter(is_active=True)
        return render(
            request, 
            'blog/post_page.html', 
            context = {
                'title': 'Blog | Post List',
                'posts': posts
            }
        )