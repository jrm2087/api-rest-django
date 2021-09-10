from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


class HelloWorld(View):
    def get(self, request):
        data = {
            'name': 'José Rodríguez L.',
            'years': 33,
            'codes': ['Python', 'PHP', 'Java', 'vue']
        }
        return render(request, 'hello_world.html', context=data)
