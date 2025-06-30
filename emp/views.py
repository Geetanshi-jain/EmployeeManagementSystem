from django.shortcuts import render, redirect,HttpResponse
from .models import Emp
from .forms import FeedbackForm,EmpForm
from .models import Testimonials

def emp_home(request):
    emps = Emp.objects.all()
    return render(request, "emp/home.html", {
        'emps': emps
    })

def add_emp(request):
    if request.method == "POST":
        # Data fetch from form
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        # Ensure required fields are not empty
        if emp_name and emp_id:
            e = Emp()
            e.name = emp_name
            e.emp_id = emp_id
            e.phone = emp_phone
            e.address = emp_address
            e.department = emp_department
            e.working = True if emp_working else False
            e.save()

            return redirect("/emp/home/")
        else:
            return HttpResponse("Name and Employee ID are required!")

    return render(request, "emp/add_emp.html")


def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home")

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request, "emp/update_emp.html",{
        'emp':emp
    })


def do_update_emp(request,emp_id):
    if request.method=='POST':
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")  
    
        e=Emp.objects.get(pk=emp_id)
        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True

        e.save()
    return redirect("/emp/home/")

def testimonials(request):
    testi=Testimonials.objects.all()

    return render(request, "emp/testimonials.html",{
        'testi':testi
    })

from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['email'])
            print(form.cleaned_data['name'])
            print(form.cleaned_data['feedback'])
            print("data saved")
            return HttpResponse(" thankyou for your feedback ") 
        else:
            return render(request, "emp/feedback.html", {'form': form})
    else:
        form = FeedbackForm()
        return render(request, "emp/feedback.html", {'form': form})
