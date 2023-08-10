from django.contrib import admin

# Register your models here.
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
  list = ('title', 'description', 'completed')

admin.site.register(Todo, TodoAdmin)