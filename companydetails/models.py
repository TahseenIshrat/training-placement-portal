from django.db import models


class Company(models.Model):

    name = models.CharField(max_length=100)

    logo = models.CharField(max_length=50, blank=True)

    industry = models.CharField(max_length=100)

    location = models.CharField(max_length=100)

    website = models.URLField(blank=True)

    hq = models.CharField(max_length=100)

    about = models.TextField()

    description = models.TextField()

    def __str__(self):
        return self.name