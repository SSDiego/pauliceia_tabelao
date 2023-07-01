from django.forms import ModelForm
from .models import form_table


# 
class formClass(ModelForm):
    class Meta:
        model = form_table
        fields = "__all__"