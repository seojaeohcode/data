from django.urls import path, include
from . import views

app_name = 'students'
urlpatterns = [
    # 학생등록페이지 호출
    path('stuWrite/',views.stuWrite,name='stuWrite'),
    # 학생등록페이지 저장
    path('stuWriteOk/',views.stuWriteOk,name='stuWriteOk'),
    # 학생전체
    path('stuList/',views.stuList,name='stuList'),
    # 상세페이지
    path('<str:s_no>/stuView/',views.stuView,name='stuView'),
]