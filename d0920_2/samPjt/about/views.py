from django.shortcuts import render

# Create your views here.
def company(request):
    return render(request, 'company.html')

def history(request):
    return render(request, 'history.html')

def recruit(request):
    return render(request, 'recruit.html')
