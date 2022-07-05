from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Problem, Solution
# Create your views here.
def index(request):
    return HttpResponse("Hello World!")
def about(request):
    context = {
    'title': 'About'
    }
    return render(request, 'online_judge/about.html', context=context)
