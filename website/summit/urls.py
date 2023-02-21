from django.urls import path
from . import views 

urlpatterns = [
    path('', views.summit_form, name='summit-form'),
    path('list/', views.SummitDataListView.as_view(), name='summit-list'),
    path('<int:pk>/update/', views.SummitDataUpdateView.as_view(), name='summit-update'),
    path('<int:pk>/delete/', views.SummitDataDeleteView.as_view(), name='summit-delete'),
]
