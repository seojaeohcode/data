from django.urls import path, include
from . import views

app_name = 'about'
urlpatterns = [
    path('company/',views.company, name='company'),
    path('history/',views.history, name='history'),
    path('recruit/',views.recruit, name='recruit'),
]
