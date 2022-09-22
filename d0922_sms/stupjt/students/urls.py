from django.urls import path, include
from . import views

app_name = 'students'
urlpatterns = [
    # 학생등록페이지 호출
    path('stuWrite/',views.stuWrite,name='stuWrite'),
    # 학생등록페이지 저장
    path('stuWriteOk/',views.stuWriteOk,name='stuWriteOk'),
]
