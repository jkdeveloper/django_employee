from __future__ import unicode_literals
import datetime
from django.db import models
from django.forms import ModelForm
from django import forms
from django.utils import timezone


department_name = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody'))

class Employee(models.Model):
	employee_name = models.CharField(max_length=200)
	dob = models.DateField('date of birth')
	doj = models.DateField('date of joining')
	email_id = models.EmailField(max_length=70)
	department = models.CharField(max_length=1, choices=department_name)
	
	def __str__(self):
		return self.employee_name
