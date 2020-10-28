from django.http import HttpResponseRedirect
from django.urls import reverse


def employee_login_required(view_func):
    """
    Decorator for views that requires employee user to be logged in.
    """

    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request, 'employee'):
            return view_func(request, *args, **kwargs)
        else:
            # User is not logged in or it is not an employee
            return HttpResponseRedirect(reverse("accounts__login") + "?next={}".format(request.path))

    wrap.__doc__=view_func.__doc__
    wrap.__name__=view_func.__name__
    return wrap