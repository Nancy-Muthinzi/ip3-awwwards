from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Project
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm

@login_required(login_url='/accounts/login/')
def home(request):
    
    return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user

    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.profile = current_user
            project.save()
        return redirect('Home')    

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form":form})        



