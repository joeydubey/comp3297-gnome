from django.db import models
from enum import Enum


class UserTypes(Enum):
    DEVELOPER = "developer"
    SCRUM_MASTER = "scrum master"
    PRODUCT_OWNER = "product owner"

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]


class ProjectStatus(Enum):
    CURRENT = "current"
    COMPLETE = "complete"

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]


class SprintStatus(Enum):
    CURRENT = "current"
    COMPLETE = "complete"

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]




class TaskStatus(Enum):
    IN_PROGRESS = "in progress"
    COMPLETE = "complete"
    NOT_YET_STARTED = "not yet started"

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]


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
    status = models.CharField(max_length=200, default=ProjectStatus.CURRENT, choices=ProjectStatus.choices())
    #users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class ProductBacklog(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SprintBacklog(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200, default=SprintStatus.CURRENT, choices=SprintStatus.choices())
    productBacklogID = models.ForeignKey(ProductBacklog, on_delete=models.CASCADE)
    #users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


#class SprintBacklog(models.Model):
#    name = models.CharField(max_length=200)
#    status = models.CharField(max_length=200, default=SprintStatus.CURRENT, choices=SprintStatus.choices())
#    productBacklogID = models.ForeignKey(ProductBacklog, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.name


class ProductBacklogItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    pointEstimate = models.IntegerField()
    productBacklogID = models.ForeignKey(ProductBacklog, on_delete=models.CASCADE)
    sprintBacklogID = models.ForeignKey(SprintBacklog, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    estimatedEffortHours = models.TimeField()
    actualEffortHours = models.TimeField()
    status = models.CharField(max_length=50, default=TaskStatus.NOT_YET_STARTED, choices=TaskStatus.choices())
    pbi = models.ForeignKey(ProductBacklogItem, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

