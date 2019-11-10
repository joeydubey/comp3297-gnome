from django.urls import path
from backtrack import views


urlpatterns = [path('projects', views.ViewAllProjects.as_view(), name='projects'),
               path('projects/<int:project>', views.ViewProject.as_view(), name='project'),
               path('projects/create-new-project', views.CreateNewProjectView.as_view(), name='newProject'),
               path('projects/product-backlog/<int:pbi>/<int:task>', views.ViewTask.as_view(), name='task'),
               path('projects/product-backlog/<int:pbi>/task/<int:pk>', views.EditTask.as_view(), name='editTask'),
               path('projects/product-backlog/<int:pbi>/task/delete-<int:pk>', views.DeleteTask.as_view(), name='deleteTask'),
               path('projects/product-backlog/pbi/<int:pk>', views.EditPBI.as_view(), name='editPBI'),
               path('projects/product-backlog/pbi/delete-<int:pk>', views.DeletePBI.as_view(), name='deletePBI'),
               path('projects/<int:project>/<int:productBacklog>/create-new-pbi', views.CreateNewPBIView.as_view(), name='newPBI'),
               path('projects/<int:project>/<int:SprintBacklog>/<int:pbi>/create-new-task', views.CreateNewTaskView.as_view(), name='newTASK'),
               path('projects/<int:project>/<int:productBacklog>/create-new-sprint', views.CreateNewSprintView.as_view(), name='newSprint'),

               path('projects/<int:project>/update-sprint/<int:pk>', views.UpdateSprintState.as_view(), name='UpdateSprintState'),

               ]
