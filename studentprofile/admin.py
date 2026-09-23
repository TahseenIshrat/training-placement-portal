from django.contrib import admin
from .models import Studentprofile


@admin.register(Studentprofile)
class StudentprofileAdmin(admin.ModelAdmin):

    fields = (
        "user",
        "degree",
        "department",
        "specialization",
        "college",
        "enrollment_number",
        "batch",
        "graduation_year",
        "cgpa",
        "tenth_percentage",
        "twelfth_percentage",
        "diploma_percentage",
        "profile_status",
    )