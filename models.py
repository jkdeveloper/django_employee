from __future__ import unicode_literals
import datetime
from django.db import models
from django.forms import ModelForm
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django import forms
from django.core.validators import EmailValidator
from django.utils import timezone


department_name = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody'))

employees = ()

class Employee(models.Model):
	
	# def validate_even(value):
	#     if value % 2 != 0:
	#         raise ValidationError(_('%(value)s is not an even number'),params={'value': value})

	employee_name = models.CharField(max_length=200)
	dob = models.DateField('date of birth')
	doj = models.DateField('date of joining')
	email_id = models.EmailField(max_length=70)
	employee_code = models.IntegerField(default=0)
	#employee_code = models.IntegerField(default=0,validators=[validate_even])
	department = models.CharField(max_length=1, choices=department_name)
	manager = models.CharField(max_length=100, choices=employees)

	def __str__(self):
		return self.employee_name