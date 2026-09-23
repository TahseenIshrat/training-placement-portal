from django.db import models
from companydetails.models import Company


class JobDrive(models.Model):

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='job_drives'
    )

    job_title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    ctc = models.CharField(max_length=50)
    openings = models.PositiveIntegerField(default=0)

    eligibility = models.TextField()
    process = models.TextField()
    rounds = models.CharField(max_length=100)

    drive_date = models.DateField()
    last_date = models.DateField()

    status = models.CharField(
        max_length=30,
        choices=[
            ("Upcoming", "Upcoming"),
            ("Open", "Open"),
            ("Closed", "Closed"),
        ],
        default="Upcoming"
    )

    def __str__(self):
        return f"{self.company.name} - {self.job_title}"