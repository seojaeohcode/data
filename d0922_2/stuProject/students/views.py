from django.shortcuts import render

# Create your views here.
def stuWrite(request):
    return render(request, 'stuWrite.html')