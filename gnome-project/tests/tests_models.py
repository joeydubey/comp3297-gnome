from django.test import TestCase
from backtrack.models import Project, ProductBacklog, SprintBacklog, ProductBacklogItem, Task

# Create your tests here.
class TestProject(TestCase):
    def setup(self):
        Project.objects.create(name="test_proj1")
        Project.objects.create(name="test_proj2")

    def test_name(self):
        proj1 = Project.objects.get_name(name="test_proj1")
        proj2 = Project.objects.get_name(name="test_proj1")
        self.assertEqual(proj1, "test_proj1")
        self.assertEqual(proj2, "test_proj2")



class TestProductBacklog(TestCase):
    def setup(self):
        ProductBacklog.objects.create()
        ProductBacklog.objects.create(name="")


class TestSprintBacklog(TestCase):
    def setup(self):
        SprintBacklog.objects.create(name="")
        SprintBacklog.objects.create(name="")



class TestProductBacklogItem(TestCase):
    def setup(self):
        ProductBacklogItem.objects.create(name="")
        ProductBacklogItem.objects.create(name="")


class Task(TestCase):
    def setup(self):
        Task.objects.create(name="")
        Task.objects.create(name="")
