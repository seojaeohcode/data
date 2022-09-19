from django.shortcuts import render

# Create your views here.
# index함수 선언
def index(request):
    return render(request,'index.html')