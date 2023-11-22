from django.urls import path
from textgen.views import homeIO, upload, upload8, io_mapping, server_error
from textgen.views import ExcelImportView, XMLImportView
urlpatterns = [
    path('homeIO', homeIO, name='homeIO'),
    path('upload', upload, name='upload'),
    path('upload8', upload8, name='upload8'),
    path('io_mapping', io_mapping, name='io_mapping'),
    path('server_error', server_error, name='server_error'),
    path('import-excel/', ExcelImportView.as_view(), name='import-excel'),
    path('import-xml/', XMLImportView.as_view(), name='import-xml'),

]

