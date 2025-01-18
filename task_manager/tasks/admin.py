from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name', 'description',
        'status', 'date', 'end_date'
    )
    search_fields = ('name', 'description',)
    list_filter = ('date',)
    empty_value_display = 'NULL'


admin.site.register(Task, TaskAdmin)