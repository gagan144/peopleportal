from django.urls import path, re_path, include

from accounts import views
from accounts.api import EmployeeResource


api_employeeResource = EmployeeResource()


urlpatterns = [
    path('login/', views.login, name="accounts__login"),
    path('logout/', views.logout, name="accounts__logout"),

    # Api
    re_path(r'^api/', include(api_employeeResource.urls)),
]