from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Project
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def home(request):
    
    return render(request, 'home.html')
