from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from peopleportal.decorators import employee_login_required
from accounts.models import Role

def home(request):
    """
    View for site home/index url.
    """
    return HttpResponseRedirect(reverse('console'))


@employee_login_required(allowed_permission_codes=None)
def console(request):
    """
    View to handle console screen.
    """

    data = {
        'list_roles': [role.to_json() for role in Role.objects.all()]
    }
    return render(request, 'console.html', data)