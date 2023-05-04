from django.urls import path
from . import views 
from django.contrib.auth.decorators import user_passes_test


urlpatterns = [
    path('', views.summit_form, name='summit-form'),
    # path('entry', views.entry, name='senf-form'),
    path('list/',  user_passes_test(lambda user: user.groups.filter(name='timesheet').exists()) (views.SummitDataListView.as_view()), name='summit-list'),
    path('<int:pk>/update/', user_passes_test(lambda user: user.groups.filter(name='timesheet').exists()) (views.SummitDataUpdateView.as_view()), name='summit-update'),
    path('<int:pk>/delete/',  user_passes_test(lambda user: user.groups.filter(name='timesheet').exists()) (views.SummitDataDeleteView.as_view()), name='summit-delete'),
    path('get/', views.SummitDataListView.as_view(), name='summit-list'),
]

