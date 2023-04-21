from django import forms
from .models import Task

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField()

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'