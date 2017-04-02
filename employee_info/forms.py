from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('employee_name', 'dob', 'doj', 'email_id', 'department')