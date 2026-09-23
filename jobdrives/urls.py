from django.urls import path
from . import views


urlpatterns = [
    path('', views.job_drives, name='jobdrives'),
]