from django.http import HttpResponse
from django.shortcuts import render
import datetime


def home(request):
    if request.method =='POST':
       check_value = request.POST.get('check')
       print(check_value)

       if check_value is None: isActive =False
       else: isActive=True
       
    date = datetime.datetime.now()
    isActive = True
    name = "LearnCodeWithGeetanshi"
    list_of_programs = [
        'WAP to check even or odd',
        'WAP to check prime number or not'
    ]

    student = {
        "student_name": "Rahul",
        "student_college": "XYZ",
        "student_city": "Lucknow"
    }

    data = {
        "date": date,
        "isActive": isActive,
        "name": name,
        "list_of_programs": list_of_programs,
        "student_data": student
    }

    return render(request, "home.html", data)


def about(request):
    return render(request,"about.html",{})

def services(request):
    return render(request,"services.html",{})

def feedback(request):
    return render(request,"emp/feedback.html",{})
