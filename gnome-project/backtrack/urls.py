from django.urls import path
from backtrack import views


urlpatterns = [path('projects', views.ViewAllProjects.as_view(), name='projects'),
               path('projects/<int:project>', views.ViewProject.as_view(), name='project'),
               path('projects/create-new-project', views.CreateNewProjectView.as_view(), name='newProject'),
               path('projects/product-backlog/<int:pbi>/<int:task>', views.ViewTask.as_view(), name='task'),
               path('projects/product-backlog/pbi/<int:pk>', views.EditPBI.as_view(), name='editPBI'),
               path('projects/product-backlog/pbi/delete-<int:pk>', views.DeletePBI.as_view(), name='deletePBI'),
               path('projects/<int:project>/<int:productBacklog>/create-new-pbi', views.CreateNewPBIView.as_view(), name='newPBI'),
               path('projects/<int:project>/<int:SprintBacklog>/<int:pbi>/create-new-task', views.CreateNewTaskView.as_view(),
                    name='newTASK'),
               ]
