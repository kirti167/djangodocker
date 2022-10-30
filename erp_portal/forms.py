from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from .models import *

class StdLeaveAppForm(forms.ModelForm):
    class Meta:
        model = StudentLeaveApp

        fields = ('content', 'to_teacher')

        widgets = {

            'content': forms.TextInput(attrs={'style': ' width: 95%; border: 1px solid grey; margin-left: 2%;margin-right: 2%;height:30px;'}),
            'to_teacher': forms.Select(attrs={'style': ' width: 95%; border: 1px solid grey; margin-left: 2%;margin-right: 2%;height:30px;'}),

        }
class AppStatusForm(forms.ModelForm):
    class Meta:
        model = AppStatus

        fields = ('status',)

        widgets = {

            'status':forms.TextInput,

        }
class TeachLeaveAppForm(forms.ModelForm):
    class Meta:
        model = TeachLeaveApp
        fields = ('content', 'to_admin',)

        widgets = {
            'content': forms.TextInput(attrs={'style': ' width: 95%; border: 1px solid grey; margin-left: 2%;margin-right: 2%;height:30px;'}),
            'to_admin': forms.Select(attrs={'style': ' width: 95%; border: 1px solid grey; margin-left: 2%;margin-right: 2%;height:30px;'}),
        }
