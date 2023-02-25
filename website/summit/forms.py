from django import forms
from .models import SummitData

class SummitForm(forms.ModelForm):
    weekday_choices = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    )

    weekday = forms.MultipleChoiceField(choices=weekday_choices, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = SummitData
        fields = ['task_name', 'task_notes', 'city', 'medium', 
        'project_code', 'summit_username', 'summit_password', 'weekday']
        widgets = {
            'summit_username': forms.TextInput(attrs={'type': 'number'}),
        }

    def get_initial(self):
        initial = super().get_initial()
        if self.instance:
            initial['weekday'] = self.instance.weekdays.split(',')
        return initial