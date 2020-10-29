from django.urls import path, re_path, include

from accounts import views
from accounts.api import EmployeeResource


api_employeeResource = EmployeeResource()


urlpatterns = [
    path('login/', views.login, name="accounts__login"),
    path('logout/', views.logout, name="accounts__logout"),

    path('employee/delete/', views.api_employee_delete, name="accounts__api_employee_delete"),

    # Api
    re_path(r'^api/', include(api_employeeResource.urls)),
]