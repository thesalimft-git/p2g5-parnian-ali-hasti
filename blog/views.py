from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(
        request, 
        'blog/home_page.html', 
        context = {
            'title': 'Blog | Home Page'
        }
    )


def posts_page(request):
    return render(
        request, 
        'blog/post_page.html', 
        context = {
            'title': 'Blog | Post List'
        }
    )