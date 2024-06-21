from django import forms
from . import models


class EmpForm(forms.ModelForm):
    class Meta:
        model = models.Employees
        fields = "__all__"
