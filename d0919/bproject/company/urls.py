from . import views
from django.urls import path,include

#app_name = 'company'
urlpatterns = [
    path('',views.company,name='company'),
]
