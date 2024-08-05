from django.urls import path
from .views import *

urlpatterns = [
    # path('stu_info/<int:pk>',student_detail,name='name'),
    # path('stu_api/',student_api,name='students_api'),
    path('StudentList/', StudentList.as_view(), name='home'),
    path("StudentDetail/<int:pk>/",StudentDetail.as_view())

]