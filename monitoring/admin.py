from django.contrib import admin
from django_celery_results.models import TaskResult

class TaskResultAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'status', 'date_done', 'task_name')
    search_fields = ('task_id', 'task_name')


admin.site.register(TaskResult, TaskResultAdmin)
