from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Project)
admin.site.register(ProductBacklog)
admin.site.register(SprintBacklog)
admin.site.register(ProductBacklogItem)
admin.site.register(Task)