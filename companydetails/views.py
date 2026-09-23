from django.shortcuts import render
from .models import Company


def companydetails(request):

    companies = Company.objects.all()

    companies_data = []

    for company in companies:
        companies_data.append({
            "id": company.id,
            "name": company.name,
            "logo": company.logo,
            "industry": company.industry,
            "location": company.location,
            "desc": company.description,
            "website": company.website,
            "about": company.about,
            "hq": company.hq,
        })

    return render(request, "companydetails.html", {
        "companies": companies_data
    })