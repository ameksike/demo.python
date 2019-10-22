from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import json

from rest_framework import generics
from .models import *
from .serializers import *



# Create your views here.
def index(request):
    context = {
        'list': [
            {'id': '1', 'name': 'Teso Tieso Tieso'},
            {'id': '2', 'name': 'Tisi Tieso Tieso'},
            {'id': '3', 'name': 'Toso Tieso Tieso'}
        ]
    }
    return render(request, 'main/index.html', context)


def detail(request, id):
    context = {
        'data': {'id': id, 'name': 'Teso Loco Deverdad'}
    }
    return render(request, 'main/detail.html', context)


def jsonEncode(request):
    context = {
        'data': {"id": 4, "name": "Teso Loco Deverdad"}
    }
    context['data']['id'] = 7
    out = json.dumps(context['data'])
    return HttpResponse(out)


def jsonDecode(request):
    context = '{"id": "55", "name": "Teso Loco Deverdad"}'
    context = json.loads(context)
    out = context['name']
    return HttpResponse(out)

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk']
        )
        return obj