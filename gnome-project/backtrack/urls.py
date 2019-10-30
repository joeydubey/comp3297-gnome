from django.urls import path
from backtrack import views


urlpatterns = [path('projects', views.ViewAllProjects.as_view(), name='projects'),
               path('projects/<int:project>', views.ViewProject.as_view(), name='project'),
               path('projects/create-new-project', views.CreateNewProjectView.as_view(), name='newProject'),
               path('projects/product-backlog/<int:pbi>/<int:task>', views.ViewTask.as_view(), name='task'),
               path('projects/product-backlog/pbi/<pk>', views.EditPBI.as_view(), name='pbi'),
               ]
