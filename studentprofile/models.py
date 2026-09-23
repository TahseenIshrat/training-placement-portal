from django.db import models
from django.contrib.auth.models import User

class Studentprofile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    # personal information
    fullname = models.CharField(max_length=100)

    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    alternate_phone_number = models.CharField(max_length=15, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)

    profile_status = models.CharField(
        max_length=20,
        default="Academic pending"
    )

    # academic information
    degree = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=150, blank=True)
    specialization = models.CharField(max_length=150, blank=True)
    college = models.CharField(max_length=200, blank=True)
    enrollment_number = models.CharField(max_length=50, blank=True)
    batch = models.CharField(max_length=20, blank=True)

    graduation_year = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    cgpa = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True
    )

    tenth_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    twelfth_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    diploma_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.fullname