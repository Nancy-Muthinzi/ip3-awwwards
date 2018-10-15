from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url('^$', views.home, name = 'home'),
    url('^today/$',views.home,name='siteToday'),
    url('^profile/(\d+)', views.profile, name='profile'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^project/(\d+)',views.project,name ='project'),
    url(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    url(r'^api/info/$', views.ProfileInfo.as_view()),
    url(r'^api/list/$', views.ProjectList.as_view())
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)