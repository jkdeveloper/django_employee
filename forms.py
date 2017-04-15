from django import forms
from .models import Employee


# def get_employees():
# 	return [(o.id, str(o)) for o in Employee.objects.all()]
choices_h = [(o.id, str(o)) for o in Employee.objects.all()]
choices_h.insert(0,(0,'Select manager'))

class EmployeeForm(forms.ModelForm):
	manager = forms.ChoiceField(choices=choices_h)
	class Meta:
		model = Employee
		# manager = forms.ChoiceField(choices=choices_h)#((o.id, str(o)) for o in Employee.objects.all()))

		#print manager,"\n\n\n\n\n\n\n\manager"
		fields = ('employee_name', 'dob', 'doj', 'email_id', 'department','employee_code','manager')