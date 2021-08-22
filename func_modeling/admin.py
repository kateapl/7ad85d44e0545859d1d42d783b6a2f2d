from django.contrib import admin

from django.contrib import admin

from .models import Function

@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    readonly_fields = ['image', ]
    fields = ('function', 'image', 'interval', 'step')
    list_display = ('function', 'image', 'interval', 'step', 'date')


