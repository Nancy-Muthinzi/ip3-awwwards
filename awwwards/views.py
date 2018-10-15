from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from .models import Project, Profile, Rate, NewsLetterRecipients
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm, NewsLetterForm
from .email import send_welcome_email
import datetime as dt
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly


@login_required(login_url='/accounts/login/')
def home(request):
    date = dt.date.today()
    form = NewsLetterForm()
    projects = Project.objects.all()
    profiles = Profile.objects.all()

    return render(request, 'home.html', {"date": date, "letterForm": form, "project": projects, "profile":profiles})


@login_required(login_url='/accounts/login/')
def profile(request, id):
    current_user = request.user
    profiles = Profile.objects.get(user=current_user)
    projects = Project.objects.all()

    return render(request, 'profile.html', {'profile': profiles, "project": projects})


def search_results(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)

        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


@login_required(login_url='/accounts/login/')
def project(request, id):

    # try:
    project = Project.objects.get(id=id)

    # except DoesNotExist:
    #     raise Http404()

    return render(request, "project.html", {"project": project})


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


class ProfileInfo(APIView):
    def get(self, request, format=None):
        all_info = Profile.objects.all()
        serializers = ProfileSerializer(all_info, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectList(APIView):
    def get(self, request, format=None):
        all_list = Project.objects.all()
        serializers = ProjectSerializer(all_list, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return ProfileInfo.objects.get(pk=pk)
        except ProfileInfo.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_info(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  

    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)      

class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return ProjectList.objects.get(pk=pk)
        except ProjectList.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectList(project)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)    

    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
