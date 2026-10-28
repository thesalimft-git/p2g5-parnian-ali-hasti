from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    
    def __str__(self) -> str:
        return self.title
    
# python manage.py makemigrations
# python manage.py migrate

# table post => models.py class Post => make, migrate => admin.py => view(model+template)