from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Studentprofile


@login_required
def profile(request):

    # Current logged-in user ka profile
    student, created = Studentprofile.objects.get_or_create(
        user=request.user,
        defaults={
            "fullname": "",
            "email": request.user.email or "",
        }
    )

    if request.method == "POST":

        form_type = request.POST.get("form_type")

        # =========================
        # PERSONAL INFORMATION
        # STUDENT ONLY
        # =========================

        if form_type == "personal":

            # Admin personal details edit nahi kar sakta
            if request.user.is_staff:
                return redirect("studentprofile")

            student.fullname = request.POST.get("fullname")
            student.date_of_birth = (
                request.POST.get("date_of_birth") or None
            )
            student.gender = request.POST.get("gender")
            student.email = request.POST.get("email")
            student.phone_number = request.POST.get("phone_number")
            student.alternate_phone_number = request.POST.get(
                "alternate_phone_number"
            )
            student.city = request.POST.get("city")
            student.state = request.POST.get("state")

            student.profile_status = "Academic Pending"

            student.save()

        # =========================
        # ACADEMIC INFORMATION
        # ADMIN ONLY
        # =========================

        elif form_type == "academic":

            # Student academic details edit nahi kar sakta
            if not request.user.is_staff:
                return redirect("studentprofile")

            student.degree = request.POST.get("degree")
            student.department = request.POST.get("department")
            student.specialization = request.POST.get("specialization")
            student.college = request.POST.get("college")
            student.enrollment_number = request.POST.get(
                "enrollment_number"
            )
            student.batch = request.POST.get("batch")

            student.graduation_year = (
                request.POST.get("graduation_year") or None
            )

            student.cgpa = request.POST.get("cgpa") or None

            student.tenth_percentage = (
                request.POST.get("tenth_percentage") or None
            )

            student.twelfth_percentage = (
                request.POST.get("twelfth_percentage") or None
            )

            student.diploma_percentage = (
                request.POST.get("diploma_percentage") or None
            )

            student.profile_status = "Completed"

            student.save()

        return redirect("studentprofile")

    return render(
        request,
        "studentprofile.html",
        {
            "student": student
        }
    )