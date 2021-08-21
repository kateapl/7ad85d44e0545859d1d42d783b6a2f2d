from django.contrib import admin

from django.contrib import admin

from .models import Function

@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    fields = ('function', 'interval', 'step')
    list_display = ('function', 'graph', 'interval', 'step', 'date')

