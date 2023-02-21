from django import forms
from .models import SummitData

class SummitForm(forms.ModelForm):
    class Meta:
        model = SummitData
        fields = ['task_name', 'task_notes', 'city', 'medium', 
        'project_code', 'summit_username', 'summit_password']
        widgets = {
            'summit_username': forms.TextInput(attrs={'type': 'number'})
        }
