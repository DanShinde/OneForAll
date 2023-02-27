from django.urls import path
from . import views

app_name = 'planner'

urlpatterns = [
    path('', views.upload_excel, name='upload_excel'), #uploadtasks/
    path('tasks/', views.task_list, name='task_list'),
    path('upload_success/', views.upload_success, name='upload_success'),
]
