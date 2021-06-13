from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone


# Create your models here.

class TodoModel(models.Model):
    title = models.CharField('title', max_length=350, unique=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy("mytodolist")
    

    def __str__(self):
        return self.title
