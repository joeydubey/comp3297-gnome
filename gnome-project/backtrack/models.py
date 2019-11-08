from django.db import models
from enum import Enum


class UserTypes(Enum):
    DEVELOPER = "developer"
    SCRUM_MASTER = "scrum master"
    PRODUCT_OWNER = "product owner"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class ProjectStatus(Enum):
    CURRENT = "current"
    COMPLETE = "complete"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class SprintStatus(Enum):
    CURRENT = "current"
    COMPLETE = "complete"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class PBIStatus(Enum):
    IN_PROGRESS = "in progress"
    COMPLETE = "complete"
    NOT_YET_STARTED = "not yet started"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class TaskStatus(Enum):
    IN_PROGRESS = "in progress"
    COMPLETE = "complete"
    NOT_YET_STARTED = "not yet started"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class User(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=UserTypes.choices())
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200, default=ProjectStatus.CURRENT.value, choices=ProjectStatus.choices())

    def save(self, *args, **kwargs):
        is_new = True if not self.id else False
        super(Project, self).save(*args, **kwargs)
        if is_new:
            product_backlog = ProductBacklog(name=self.name+" product backlog", project=self)
            product_backlog.save()

    def __str__(self):
        return self.name


class ProductBacklog(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def pbiList(self):
        return ProductBacklogItem.objects.filter(productBacklogID=self.id)

class SprintBacklog(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200, default=SprintStatus.CURRENT.value, choices=SprintStatus.choices())
    productBacklogID = models.ForeignKey(ProductBacklog, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

    def pbiList(self):
        return ProductBacklogItem.objects.filter(sprintBacklogID=self.id)
   
    @property
    def sprint_cummulative_effort_hours(self):
        x = 0 
        for PBI in self.pbiList():
            x += PBI.tasks_cummulative_effort_hours
        return x

    @property
    def sprint_actual_effort_hours(self):
        x = 0 
        for PBI in self.pbiList():
            x += PBI.tasks_actual_effort_hours
        return x

    @property
    def sprint_work_remaining(self):
        return self.sprint_cummulative_effort_hours - self.sprint_actual_effort_hours

class ProductBacklogItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    pointEstimate = models.IntegerField(blank=True, null=True)
    productBacklogID = models.ForeignKey(ProductBacklog, on_delete=models.CASCADE)
    sprintBacklogID = models.ForeignKey(SprintBacklog, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=50, default=PBIStatus.NOT_YET_STARTED.value, choices=PBIStatus.choices())

    def __str__(self):
        return self.name

    def tasks(self):
        return Task.objects.filter(pbi=self)

    def tasks_complete(self):
        return Task.objects.filter(pbi=self, status=TaskStatus.COMPLETE.value)

    def tasks_in_progress(self):
        return Task.objects.filter(pbi=self, status=TaskStatus.IN_PROGRESS.value)

    def tasks_not_yet_started(self):
        return Task.objects.filter(pbi=self.pk, status=TaskStatus.NOT_YET_STARTED.value)
    
    @property
    def tasks_cummulative_effort_hours(self):
        x = 0 
        for Task in self.tasks():
            if (type(Task.estimatedEffortHours) is float):
                x += Task.estimatedEffortHours
        return x

    @property
    def tasks_actual_effort_hours(self):
        x = 0 
        for Task in self.tasks():
            if (type(Task.actualEffortHours) is float):
                x += Task.actualEffortHours
        return x
    @property
    def tasks_work_remaining(self):
        return self.tasks_cummulative_effort_hours - self.tasks_actual_effort_hours
    
    #def addToSprint(self):


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    estimatedEffortHours = models.FloatField()
    actualEffortHours = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=50, default=TaskStatus.NOT_YET_STARTED.value, choices=TaskStatus.choices())
    pbi = models.ForeignKey(ProductBacklogItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def tasks_estimated_effort_hours(self):
        return self.estimatedEffortHours

