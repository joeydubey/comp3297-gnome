from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200, default='Not yet started')

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name


class ProductBacklog(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SprintBacklog(ProductBacklog):

    def __str__(self):
        return self.name


class ProductBacklogItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    pointEstimate = models.IntegerField()
    productBacklog = models.ForeignKey(ProductBacklog, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=200)
    sprintBacklog = models.ForeignKey(SprintBacklog, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    estimatedEffortHours = models.TimeField()
    actualEffortHours = models.TimeField()
    status = models.CharField(max_length=50)
    pbi = models.ForeignKey(ProductBacklogItem, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
