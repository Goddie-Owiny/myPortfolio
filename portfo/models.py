from django.db import models

# Create your models here.
class Blog(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(default=None, max_length=50, blank=True)
    description = models.TextField(default=None, blank=True)
    
