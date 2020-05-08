from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


def home(request):
    data = Project.objects.all()
    return render(request,'portfolio/home.html',{'projects':data})
# Create your views here.
