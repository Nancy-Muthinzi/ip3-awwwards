from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Project
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm, NewsLetterForm
from .email import send_welcome_email
import datetime as dt


@login_required(login_url='/accounts/login/')
def home(request):
    date = dt.date.today()
    day = convert_dates(date)
    print('date')
    print(date)

    # if request.method == 'POST':
    #     form = NewsLetterForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['your_name']
    #         email = form.cleaned_data['email']

    #         recipient = NewsLetterRecipients(name=name, email=email)
    #         recipient.save()
    #         send_welcome_email(name, email)

    return render(request, 'home.html', {"date": date})


def convert_dates(dates):
    day_number = dt.date.weekday(dates)
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', "Sunday"]
    day = days[day_number]
    return day


@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user

    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = current_user
            project.save()
        return redirect('Home')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})
