from django.conf.urls import url
from . import views


app_name = 'employee_info'

urlpatterns = [
    url(r'^employee/new/$', views.employee_new, name='employee_new'),
    url(r'^employee/list/$', views.employee_list, name='employee_list'),
    url(r'^ajax_employee$', views.ajax_employee, name='ajax_employee'),
    #url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
]