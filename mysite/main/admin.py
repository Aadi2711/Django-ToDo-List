import imp
from django.contrib import admin

from .models import Items, ToDoList
# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Items)
