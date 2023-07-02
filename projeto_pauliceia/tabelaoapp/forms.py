from django.forms import ModelForm, DateInput
from .models import form_table


class formClass(ModelForm):
    class Meta:
        model = form_table
        fields = "__all__"
        widgets = {
            'dt_realizacao': DateInput(attrs={'type': 'date'}),
        }