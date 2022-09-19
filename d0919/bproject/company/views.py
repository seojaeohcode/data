from django.shortcuts import render

# Create your views here.
def ceo(request):
    return render(request,'ceo.html')

def philosophy(request):
    return render(request, 'philosophy.html')