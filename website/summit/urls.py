from django.urls import path
from . import views 

urlpatterns = [
    path('', views.summit_form, name='summit-form'),
    path('list', views.SummitDataListView, name='summit-list'),
]
