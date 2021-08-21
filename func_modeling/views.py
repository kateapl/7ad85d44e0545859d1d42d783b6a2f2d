from django.shortcuts import render

from .models import Function


def index(request):
    function_list = Function.objects.order_by('date')
    context = {'function_list': function_list}
    return render(request, 'func_modeling/index.html', context)