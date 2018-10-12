from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.home, name = 'home'),
    url('^today/$',views.home,name='home'),
    url(r'^new/project$', views.new_project, name='new-project')
]