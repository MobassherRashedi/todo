from django.contrib import admin
from .models import TodoModel
# Register your models here.

class TodoModelAdmin(admin.ModelAdmin):
        list_display = ['title','published','updated']

admin.site.register(TodoModel,TodoModelAdmin)