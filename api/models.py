from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,blank=True,null=True,on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    started = models.DateTimeField(blank=True, null=True)
    ended = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(max_length=20, default='created')
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title