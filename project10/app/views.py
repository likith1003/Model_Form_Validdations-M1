from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
from .models import *
# Create your views here.

def insert_skool(request):
    ESFO = SchoolForm()
    d = {'ESFO': ESFO}
    if request.method == 'POST':
        SFO = SchoolForm(request.POST)
        if SFO.is_valid():
            sname = SFO.cleaned_data['sname']
            princy = SFO.cleaned_data['princy']
            contact = SFO.cleaned_data['contact']
            loc = SFO.cleaned_data['loc']
            school = School(sname=sname, princy=princy, contact=contact, loc=loc)
            school.save()
            return HttpResponse('School Created')
        return HttpResponse('Invalid Data')
    return render(request, 'insert_skool.html', d)


def register(request):
    ERFO = RegisterForm()
    d = {'ERFO': ERFO}
    if request.method == 'POST':
        RFDO = RegisterForm(request.POST)
        if RFDO.is_valid():
            RFDO.save()
            return HttpResponse('registration Done')
        return HttpResponse('Invalid Data')

    return render(request, 'register.html', d)


def student(request):
    ESFO = StudentForm()
    d = {'ESFO':ESFO}
    if request.method == 'POST':
        SFDO = StudentForm(request.POST)
        if SFDO.is_valid():
            sname = SFDO.cleaned_data['sname']
            stdname=SFDO.cleaned_data['stdname']
            SO = Student(sname=sname, stdname=stdname)
            SO.save()
            return HttpResponse('Done.....')
        return HttpResponse('Noo.....')
    
    return render(request, 'student.html', d)