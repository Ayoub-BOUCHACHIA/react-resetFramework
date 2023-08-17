from django.contrib import admin

# Register your models here.
from .models import Todo, EurUsd

class TodoAdmin(admin.ModelAdmin):
  list = ('title', 'description', 'completed')

class EurUsdAdmin(admin.ModelAdmin):
  list = ('id', 'timestamp', 'open', 'close', 'high', 'low', 'volume', 'date', 'month', 'day', 'hour', 'minute', 'minute', 'direction')

admin.site.register(Todo, TodoAdmin)
admin.site.register(EurUsd, EurUsdAdmin)