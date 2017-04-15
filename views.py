from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Employee
from .forms import EmployeeForm
from django.shortcuts import redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
import datetime


def employee_new(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
			employee = form.save(commit=False)
			employee.employee_name = request.POST.get('employee_name')
			dob = request.POST.get('dob')
			doj = request.POST.get('doj')
			employee.dob = dob[6:] + "-" + dob[3:5] + "-" + dob[:2]
			employee.doj = doj[6:] + "-" + doj[3:5] + "-" + doj[:2]
			employee.email_id = request.POST.get('email_id')
			employee.department = request.POST.get('department')
			employee.save()
			employees = Employee.objects.all()
			return render(request, 'employee_info/employee_list.html', {'employees': employees})
    else:
        form = EmployeeForm()
    return render(request, 'employee_info/employee_new.html', {'form': form})



def employee_list(request):
	#print "inside employee_list"
	employees = Employee.objects.order_by('dob')
	return render(request, 'employee_info/employee_list.html', {'employees': employees})   


@csrf_exempt
def ajax_employee(request):
	employee = Employee.objects.get(employee_name=request.GET.get('message',None))
	data = {
	    'is_taken': Employee.objects.filter(employee_name__iexact=request.GET.get('message',None)).exists()
	}
	return JsonResponse(data)


@csrf_exempt
def ajax_new_employee_form(request):
	return render(request, 'employee_info/employee_new.html', {'form': EmployeeForm()})
