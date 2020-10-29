from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from accounts.models import Employee
from peopleportal.decorators import employee_login_required
from utilities.api_utils import ApiResponse
from accounts.forms import EmployeeForm


def login(request):
    """
    View to handle user login.
    """

    data={
        'next': request.GET.get('next',None)
    }

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            try:
                # Check if this user is an employee
                employee = user.employee

                # User is an employee and active; Login and create session
                auth.login(request, user)
                next = request.GET.get('next', None)
                if next and next != '':
                    return HttpResponseRedirect(request.GET['next'])
                else:
                    return HttpResponseRedirect(reverse('console'))

            except Employee.DoesNotExist:
                data['login_fail'] = True
                data['username'] = username
        else:
            data['login_fail'] = True
            data['username'] = username

    return render(request, 'accounts/login.html', data)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('accounts__login'))


# ----- Employee CRUD -----

@employee_login_required(allowed_permission_codes=['employee_delete'])
def api_employee_delete(request):
    """
    API to to delete an employee.
    """

    if request.method.lower() == 'post':
        employee_id = int(request.POST['employee_id'])

        try:
            employee = Employee.objects.get(id=employee_id)

            employee.delete()

            return ApiResponse.http(status=ApiResponse.ST_SUCCESS, message='Employee successfully deleted')

        except Employee.DoesNotExist:
            return ApiResponse.http(status=ApiResponse.ST_FAILED, message='Invalid employee.')
    else:
        return ApiResponse.http(status=ApiResponse.ST_FORBIDDEN, message='Use Post!')


@employee_login_required(allowed_permission_codes=['employee_create'])
def api_employee_create(request):
    """
    API to to create an employee.
    """

    if request.method.lower() == 'post':

        data = request.POST.dict()
        form_employee = EmployeeForm(data=data)

        if form_employee.is_valid():
            new_employee = form_employee.save()
            return ApiResponse.http(status=ApiResponse.ST_SUCCESS, message='New Employee successfully created!')
        else:
            errors = dict(form_employee.errors)
            return ApiResponse.http(status=ApiResponse.ST_FAILED, message='Validation errors.', errors=errors)
    else:
        return ApiResponse.http(status=ApiResponse.ST_FORBIDDEN, message='Use Post!')


@employee_login_required(allowed_permission_codes=['employee_edit'])
def api_employee_edit(request):
    """
    API to to edit an employee.
    """

    if request.method.lower() == 'post':

        data = request.POST.dict()
        employee_id = int(request.POST['employee_id'])

        try:
            employee = Employee.objects.get(id=employee_id)

            # TODO: Validate employee details
            # TODO: Update employee details in db

            return ApiResponse.http(
                status=ApiResponse.ST_SUCCESS,
                message='Success! Dummy success response indicating that db was updated.',
                emp_id=employee.employee_id
            )
        except Employee.DoesNotExist:
            return ApiResponse.http(status=ApiResponse.ST_FAILED, message='Invalid employee.')
    else:
        return ApiResponse.http(status=ApiResponse.ST_FORBIDDEN, message='Use Post!')
# ----- /Employee CRUD -----
