from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from .models import Project, Profile, Rate, NewsLetterRecipients
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm, NewsLetterForm
from .email import send_welcome_email
import datetime as dt


@login_required(login_url='/accounts/login/')
def home(request):
    date = dt.date.today()
    form = NewsLetterForm()
    projects = Project.objects.all()

    return render(request, 'home.html', {"date": date, "letterForm":form, "project":projects})

@login_required(login_url='/accounts/login/')
def profile(request, id):
    current_user = request.user
    profiles = Profile.objects.get(user=current_user)
    projects = Project.objects.all()
    images = Image.objects.filter(user=current_user)

    return render(request, 'profile.html', {'profile': profiles, "project":projects, "images": images})

def search_results(request):    
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)

        message = f"{search_term}"

        return render(request, 'search.html', {"message":message, "projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})    


@login_required(login_url='/accounts/login/')
def project(request, article_id):
    
    try:
        project = Project.objects.get(id = project_id)
    
    except DoesNotExist:
        raise Http404()
    
    return render(request, "project.html", {"project":project})   

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

def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to our mailing list'}
    return JsonResponse(data)