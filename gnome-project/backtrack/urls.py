from django.urls import path
from backtrack import views


urlpatterns = [path('projects', views.ViewProjects.as_view(), name='projects'),
               path('projects/<int:project>', views.ViewProject.as_view(), name='project'),
               path('projects/create-new-project', views.CreateNewProjectView, name='newProject')
               ]
