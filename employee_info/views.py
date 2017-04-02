from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Employee
from .forms import EmployeeForm
from django.shortcuts import redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView



def employee_new(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
			employee = form.save(commit=False)
			employee.employee_name = "request.employee_name"
			employee.dob = "2017-03-31"
			employee.doj = "2017-03-31"
			employee.email_id = "request.email_id"
			employee.department = 'Male'
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
	print request,"request\n\n\n\n\n\n",request.GET.get("message", None)
	employee = Employee.objects.get(employee_name=request.GET.get('message',None))
	print employee,"efdfs"
	data = {
	    'is_taken': Employee.objects.filter(employee_name__iexact=request.GET.get('message',None)).exists()
	}
	return JsonResponse(data)