from django.conf.urls import url
from .views import EmployeeList,EmployeeDetail#employee_list
urlpatterns=[
    url(r'^emp/$',EmployeeList.as_view()),
    url(r'^emp/(?P<pk>\d+)/$',EmployeeDetail.as_view()),

]