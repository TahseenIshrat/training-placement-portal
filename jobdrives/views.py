from django.shortcuts import render
from .models import JobDrive


def job_drives(request):

    drive_queryset = JobDrive.objects.select_related('company').all()

    drives = []

    for drive in drive_queryset:

        drives.append({
            "id": drive.id,
            "job_title": drive.job_title,
            "description": drive.description,
            "ctc": drive.ctc,
            "openings": drive.openings,
            "eligibility": drive.eligibility,
            "process": drive.process,
            "rounds": drive.rounds,

            "drive_date": (
                drive.drive_date.isoformat()
                if drive.drive_date
                else ""
            ),

            "last_date": (
                drive.last_date.isoformat()
                if drive.last_date
                else ""
            ),

            "status": drive.status,

            "company": {
                "id": drive.company.id,
                "name": drive.company.name,
                "logo": drive.company.logo,
                "industry": drive.company.industry,
                "location": drive.company.location,
                "website": drive.company.website,
                "hq": drive.company.hq,
            }
        })

    return render(
        request,
        'jobdrives.html',
        {
            'drives': drives
        }
    )