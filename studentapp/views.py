from django.shortcuts import render,redirect
from .models import *
from .forms import StudentForm


def display_studentdata(request):
    category = Course.objects.all()
    coursefilter = None
    print("ll")
    data = Student.objects.all()
    if request.method == 'POST':
        coursefilter = request.POST.get('categories')
        print("kk")

        if coursefilter:
            courseselected = Course.objects.filter(name=coursefilter).first()
            if courseselected:
                data = Student.objects.filter(course=courseselected)
        
    
    return render(request, 'index.html', {"data":data,"coursefilter":coursefilter,"category":category})

def student_registration(request):
    if request.method == 'POST':
        form_obj = StudentForm(request.POST)
        if form_obj.is_valid():
        
            form_obj.save()
            return redirect('/')
        else:
            print(form_obj.errors)

    return render(request, 'registration.html',{'form':StudentForm})

