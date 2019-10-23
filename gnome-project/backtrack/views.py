from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from orders.models import Project, ProductBacklog, SprintBacklog

# Create your views here.


class ViewProjects(TemplateView):
    template_name = "project_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = Project.objects.all()
        return context


class ViewProject(TemplateView):
    template_name = "project.html"

    def get_context_data(self, **kwargs):
        project = self.kwargs['project']
        context = super().get_context_data(**kwargs)
        context['project'] = Project.objects.all(pk = project)
        return context


class ProjectsViewAll(ListView):
    template_name = "project_list.html"
    model = Project