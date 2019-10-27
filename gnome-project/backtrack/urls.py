from django.urls import path
from backtrack import views
from django.views.generic.edit import CreateView


urlpatterns = [path('projects', views.ViewAllProjects.as_view(), name='projects'),
               path('projects/<int:project>', views.ViewProject.as_view(), name='project'),
               path('projects/create-new-project', views.CreateNewProjectView.as_view(), name='newProject'),
               path('projects/<int:project>/<int:productBacklog>/create-new-pbi', views.CreateNewPBIView.as_view(), name='newPBI'),
               ]
