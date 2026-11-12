from django.shortcuts import render
from django.contrib.auth import authenticate, login


# Create your views here.
def login_page_view(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(
            request, 
            username=username, 
            password=password
        )

        if user:
            login(request, user)
            # return redirect('home')  # change to your target URL name
            
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