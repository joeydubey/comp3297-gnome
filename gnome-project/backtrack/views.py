from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from backtrack.models import Project, ProductBacklog, SprintBacklog, ProjectStatus, SprintStatus, ProductBacklogItem
import logging

from django.views.generic.edit import CreateView

# Create your views here.

logging.basicConfig(level=logging.DEBUG)


class ViewAllProjects(TemplateView):
    template_name = "project_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_list1'] = Project.objects.filter(status=ProjectStatus.CURRENT.name)
        context['project_list2'] = Project.objects.filter(status=ProjectStatus.COMPLETE.name)
        return context


class ViewProject(TemplateView):
    template_name = "project.html"

    def get_context_data(self, **kwargs):
        project_id = self.kwargs['project']
        context = super().get_context_data(**kwargs)
        project = Project.objects.filter(id=project_id)
        product_backlog_list = ProductBacklog.objects.filter(project_id=project_id)

        if len(product_backlog_list) != 1:
            print("A PROJECT SHOULD ONLY HAVE ONE PRODUCT BACKLOG")

        product_backlog = product_backlog_list[0]
        sprint_backlogs = SprintBacklog.objects.filter(productBacklogID=product_backlog.id)
        sprint_list_current = sprint_backlogs.filter(status=SprintStatus.CURRENT.name)

        if len(sprint_list_current) != 1:
            print("A PRojECt SHOULD ONLY HAVE ONE CURRENT SPRINT")

        context["sprint_current"] = sprint_list_current[0]
        sprint_current_id = sprint_list_current[0].id

        context['pbi_sprint_current_list'] = ProductBacklogItem.objects.filter(sprintBacklogID=sprint_current_id)
        context['sprint_list_done'] = sprint_backlogs.filter(status=SprintStatus.COMPLETE.name)

        context['pbis_product_backlog_list'] = ProductBacklogItem.objects.filter(productBacklogID=product_backlog.id)
        print(context['pbis_product_backlog_list'])

        return context


class CreateNewProjectView(CreateView):
    template_name = "project_form.html"
    model = Project
    fields = ['name', 'status']


