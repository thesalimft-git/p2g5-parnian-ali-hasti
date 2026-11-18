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
from .views import home_page, posts_page

urlpatterns = [
    path('posts/', posts_page),
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
                    # CORS hacking


<ul>
    {% for post in posts %}
        <li>{{ post.title }}</li>
    {% endfor %}
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
```