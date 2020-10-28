from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from accounts.models import Employee

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
