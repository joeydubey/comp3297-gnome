from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse
from django.views.generic.list import ListView
from backtrack.models import Project, ProductBacklog, SprintBacklog, ProjectStatus, SprintStatus, ProductBacklogItem, Task, TaskStatus
import logging
from django.shortcuts import get_object_or_404


from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

logging.basicConfig(level=logging.DEBUG)


class DeletePBI(DeleteView):
    template_name = "productbacklogitem_confirm_delete.html"
    model = ProductBacklogItem
    slug_field = 'pbi'

    def get_success_url(self):
        pbi_ID = self.object.id
        pbi = ProductBacklogItem.objects.get(id=pbi_ID)
        project = Project.objects.get(id=pbi.productBacklogID.project_id)
        return reverse('project', args=(project.id,))


class EditPBI(UpdateView):
    template_name = "pbi.html"

    model = ProductBacklogItem
    slug_field = "pbi"
    fields = ['name', 'description', 'pointEstimate', 'status']

    def get_success_url(self):
        pbi_ID = self.object.id
        pbi = ProductBacklogItem.objects.get(id=pbi_ID)
        project = Project.objects.get(id=pbi.productBacklogID.project_id)
        return reverse('project', args=(project.id,))


class ViewAllProjects(TemplateView):
    template_name = "project_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_list1'] = Project.objects.filter(status=ProjectStatus.CURRENT.value)
        context['project_list2'] = Project.objects.filter(status=ProjectStatus.COMPLETE.value)
        return context


class ViewTask(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_id = self.kwargs['task']
        context['task'] = Task.objects.filter(id=task_id)[0]
        return context


class ViewProject(TemplateView):
    template_name = "project.html"

    def get_context_data(self, **kwargs):
        project_id = self.kwargs['project']
        context = super().get_context_data(**kwargs)
        context['project'] = Project.objects.filter(id=project_id)[0]
        product_backlog_list = ProductBacklog.objects.filter(project_id=project_id)

        if len(product_backlog_list) != 1:
            print("A PROJECT SHOULD ONLY HAVE ONE PRODUCT BACKLOG")

        context['product_backlog'] = product_backlog_list[0]
        sprint_backlogs = SprintBacklog.objects.filter(productBacklogID=context['product_backlog'].id)

        if len(sprint_backlogs) != 0:
            sprint_list_current = sprint_backlogs.filter(status=SprintStatus.CURRENT.value)
            print(sprint_list_current)

            if len(sprint_list_current) > 1:
                print("A PROJECT SHOULD ONLY HAVE ONE CURRENT SPRINT")

            if len(sprint_list_current) != 0:
                context["sprint_current"] = sprint_list_current[0]

            if len(sprint_list_current) == 0:
                print("create a new sprint")
            
            sprint_list_done = sprint_backlogs.filter(status=SprintStatus.COMPLETE.name)

            context['sprint_list_done'] = sprint_list_done

            #context['pbis_product_backlog_list'] = ProductBacklogItem.objects.filter(productBacklogID=product_backlog.id)
            context['product_backlog'] = product_backlog
            return context


class CreateNewProjectView(CreateView):
    template_name = "project_form.html"
    model = Project
    fields = ['name', 'status']

    def get_success_url(self):
        return reverse('project', args=(self.object.id,))


class CreateNewPBIView(CreateView):
    template_name = "pbi_form.html"
    model = ProductBacklogItem
    fields = ['name', 'description']

    def form_valid(self, form):
        product_backlogID = get_object_or_404(ProductBacklog, id=self.kwargs['productBacklog'])
        form.instance.productBacklogID = product_backlogID
        return super(CreateNewPBIView, self).form_valid(form)

    def get_success_url(self):
        pbi_ID = self.object.id
        pbi = ProductBacklogItem.objects.get(id=pbi_ID)
        project = Project.objects.get(id=pbi.productBacklogID.project_id)
        return reverse('project', args=(project.id,))


class CreateNewTaskView(CreateView):
    template_name = "task_form.html"
    model = Task
    fields = ['name', 'description', 'estimatedEffortHours']

    def form_valid(self, form):
        pbi_ID = get_object_or_404(ProductBacklogItem, id=self.kwargs['pbi'])
        form.instance.pbi = pbi_ID
        return super(CreateNewTaskView, self).form_valid(form)

    def get_success_url(self):
        task_ID = self.object.id
        task = Task.objects.get(id=task_ID)
        project = Project.objects.get(id=task.pbi.productBacklogID.project_id)
        return reverse('project', args=(project.id,))


class CreateNewSprintView(CreateView):
    template_name = "sprint_form.html"
    model = SprintBacklog
    fields = ['name']
    print("do you even get here")

    def form_valid(self, form):
        product_backlog = get_object_or_404(ProductBacklog, id=self.kwargs['productBacklog'])
        form.instance.productBacklogID = product_backlog
        return super(CreateNewSprintView, self).form_valid(form)

    def get_success_url(self):
        productBacklogID = self.object.productBacklogID
        print(productBacklogID)
        productBacklog = ProductBacklog.objects.get(id=productBacklogID.id)
        project = Project.objects.get(id=productBacklog.project.id)
        print(project)
        return reverse('project', args=(project.id,))
