from django.urls import path
from backtrack import views


urlpatterns = [path('projects', views.ViewProjects2.as_view(), name='projects'),
               path('projects/<int:project>', views.ViewProject.as_view(), name='project'),
               path('projects/create-new-project', views.CreateNewProjectView, name='newProject'),
            path('projects/create-new-project2', views.CreateNewProjectView2, name='newProject2')
               ]
