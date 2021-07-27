from django.contrib import admin
from .models import ToDo

class ToDoAmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(ToDo, ToDoAmin)