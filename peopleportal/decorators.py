from django.http import HttpResponseRedirect
from django.urls import reverse

from accounts.auth import has_authorization


def employee_login_required(allowed_permission_codes=None, *args, **kwargs):
    """
    Decorator for views that requires employee user to be logged in.
    """

    def actual_decorator(view_func):
        def wrap(request, *args, **kwargs):
            is_valid = has_authorization(request=request, allowed_permission_codes=allowed_permission_codes)
            if is_valid:
                return view_func(request, *args, **kwargs)
            else:
                # User is not logged in or it is not an employee
                return HttpResponseRedirect(reverse("accounts__login") + "?next={}".format(request.path))

        wrap.__doc__=view_func.__doc__
        wrap.__name__=view_func.__name__
        return wrap

    return actual_decorator


# def employee_login_required(view_func, allowed_permission_codes=None):
#     """
#     Decorator for views that requires employee user to be logged in.
#     """
#
#     def wrap(request, *args, **kwargs):
#         if request.user.is_authenticated and hasattr(request, 'employee'):
#             return view_func(request, *args, **kwargs)
#         else:
#             # User is not logged in or it is not an employee
#             return HttpResponseRedirect(reverse("accounts__login") + "?next={}".format(request.path))
#
#     wrap.__doc__=view_func.__doc__
#     wrap.__name__=view_func.__name__
#     return wrap