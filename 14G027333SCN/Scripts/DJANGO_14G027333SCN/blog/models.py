from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length= 200)
    author = get_user_model(Foreign key)
    text = models.TextField(max_length=100)
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()

