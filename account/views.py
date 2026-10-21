from django.shortcuts import render

# Create your views here.
def login_page_view(request):
    return render(
        request, 
        'account/login.html', 
        {'title': 'Blog | Login'}
    )

def logout_page_view(request):
    return render(
        request, 
        'account/logout.html', 
        {'title': 'Blog | Logout'}
    )

def register_page_view(request):
    return render(
        request, 
        'account/register.html', 
        {'title': 'Blog | Register'}
    )