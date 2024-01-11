from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def create_student(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SDFO=StudentForm(request.POST)
        if SDFO.is_valid():
            SDFO.save()

            QLSO=Student.objects.all()
            d1={'QLSO':QLSO}
            return render(request,'display_student.html',d1)
        else:
            return HttpResponse('Invalid data')
        
    return render(request,'create_student.html',d)