
from django.contrib import admin
from .models import JobDrive


@admin.register(JobDrive)
class JobDriveAdmin(admin.ModelAdmin):
    list_display = (
        'job_title',
        'company',
        'ctc',
        'openings',
        'drive_date',
        'last_date',
        'status',
    )

    list_filter = ('status', 'company')
    search_fields = ('job_title', 'company__name')