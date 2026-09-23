from django.urls import path
from . import views
urlpatterns = [
    path('companydetails/', views.companydetails, name='companydetails'),
]