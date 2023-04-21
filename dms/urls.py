from django.urls import path
from . import views

app_name = 'dms'

urlpatterns = [
    path('', views.ProjectList.as_view(), name='project_list'),
    path('project/create/', views.ProjectCreate.as_view(), name='ProjectCreate'),
    path('project/<int:pk>/', views.ProjectDetail.as_view(), name='project_detail'),
    path('project/<int:pk>/update/', views.ProjectUpdate.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project_delete'),
    path('task/<int:pk>/request_validation/', views.request_validation, name='request_validation')

]
 