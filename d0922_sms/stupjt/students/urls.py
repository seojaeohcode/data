from django.urls import path, include
from . import views

app_name = ''
urlpatterns = [
    path('stuWrite/',views.stuWrite,name='stuWrite'),
]
