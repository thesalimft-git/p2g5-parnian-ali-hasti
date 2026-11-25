## Install django and Create Project

1- Create environment
```bash
python -m venv .venv
source .venv/Scripts/activate
```

2- Install django on venv
```bash
pip install Django
```

3- Create a project
```bash
django-admin startapp core .
```

## Create App (e.g. blog app)

1- Create the main app
```bash
python manage.py startapp blog
```

2- Add setting
In setting.py add name new app [blog] to INSTALLED_APPS
```python
INSTALLED_APPS = [
#    ...
    'blog',
]
```

3- Add new path to urls.py file in [blog] app.
```python
from django.urls import path
from .views import home_page, post_list_view

urlpatterns = [
    path('posts/', post_list_view),
]
```

4- Present urls.py from app blog to core app
```python
from django.urls import include

urlpatterns = [
    # ...
    path('', include('blog.urls')),
    # ...
]
```


## Define view in views.py

### A: Use Render
```python
from .models import Post
   
def post_list_view(request):
    posts = Post.objects.filter(is_active=True)
    
    return render(
        request, 
        'blog/post_page.html', 
        context = {
            'posts': posts
        }
    ) 
```

### B: Use HttpResponse
```python
from django.http import HttpResponse

def post_list_view(request):
    return HttpResponse('salam')
```

### Class Base view

not yet

## Template
1- Create a directory in root called "templates"
2- Create a file called "base.html"
3- Define some new blocks in base.html with unique name

example of "template tags" of Django Template

```html
{% include 'topbar.html' %}
{% include 'mobile_menu.html' %}
{% block <unique name> %}{% endblock <unique name> %}
```

4- Use Extend for any other html file
e.g post-list_page.html
```html
{% extend 'base.html' %}
{% block <unique name> %}
    content from post list page 
{% endblock <unique name> %}
```

5- Add root templates directory to settings.py

```python
TEMPLATES = [
    {
        # ...
        'DIRS': [ BASE_DIR / 'templates' ],
        # ...
    }
]
```

## Django template tags

```python
if, for, {{}}
insert
url

{% extend 'base.html' %}
{% block <unique name> %} ...
{% csrf_token %}    # send form data with POST method
                    # CROSS hacking


<ul>
    {% for post in posts %}
        <li>{{ post.title }}</li>
    {% endfor %}
    # {% /for %}
</ul>



<ul>
  {% if user.is_authenticated %}
    <p> you are logged in </p>
  {% else %}
    <p> you should logged in </p>
  {% endif %}
</ul>



# some django template FILTER (Modifier)
{{ value|title }} # value is 'salam ALI' ==> 'Salam Ali'



{{ value|add:"2" }}
# If value is 4, then the output will be 6.

{{ value|capfirst }} 
# If value is "hello django", the output will be "Hello django".


{{ value|floatformat:3 }}
34.23234 => 34.232


{{ value|floatformat }}
34.23234 => 34.2



{{ posts|length }} # 3 = number of items in list


{{ now|time:"H:i" }}

```



## Model
Create a class called TableName, singular, define field.

- Table => class, object, for example User, Post, Product, ...

- Record => a row of data, an object, one post.

- Field => name column (e.g for POST table, title, content, writer, published_date)


```python
from django.db import models

# create the table POST
class Post(models.Model):
    # create fields
    title = models.CharField(
        max_length=150, 
        null=True, 
        blank=True
    )

    # to show the title of post in admin panel
    def __str__(self) -> str:
        return self.title
```





## Login , logout

1- write url

```python
from django.urls import path
from .views import login_page_view, logout_page_view, register_page_view

urlpatterns = [
    path('login/', login_page_view),
    path('logout/', logout_page_view),
    path('register/', register_page_view),
]
```

2- write views
```python
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
```

3- redirect after logout 
```python
# add name to each path: urls.py
path('login/', login_page_view, name='login-page'),

# redirect if needed: views.py
from django.shortcuts import render, redirect

def logout_page_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login-page')
    else:
        return render(
            request, 
            'account/logout.html', 
            {'title': 'Blog | Logout'}
        )
```



## Http methods

url => /posts/ ...
- get     => list posts
- post    => create new post

url => /posts/pk ...
- get       => retrieve, detail a post
- delete    => delete a post
- put       => update post
