import re
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from students.models import Student

# Create your views here.
def stuWrite(request):
    return render(request, 'stuWrite.html')

def stuWriteOk(request):
    s_name = request.POST.get('name')
    s_major = request.POST.get('major')
    s_age = request.POST.get('age')
    s_grade = request.POST.get('grade')
    s_gender = request.POST.get('gender')
    print("views :"+s_name)
    qs = Student(s_name=s_name,s_major=s_major,s_age=s_age,s_grade=s_grade,s_gender=s_gender)
    qs.save()
    
    print("write Ok!!")
    
    return HttpResponseRedirect(reverse('index'))

def stuList(request):
    qs = Student.objects.all()
    #역순정렬로 데이터 받아오기 qs = Student.objects.order_by('-s_no')
    count = qs.count()
    context = {'stuList':qs, 'count':count}#dic타입으로 전송
    return render(request, 'stuList.html', context)