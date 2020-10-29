from tastypie.authentication import SessionAuthentication


class EmployeeAuthentication(SessionAuthentication):
    """
    Django tastypie session authentication for employee user.
    This also includes authorization and sets permissions etc.
    """

    def __init__(self, list_permission_codes=None):
        super().__init__()
        self.list_permission_codes = list_permission_codes

    def is_authenticated(self, request, **kwargs):
        is_valid = False

        # Check user is logged in and is an employee
        if request.user.is_authenticated and hasattr(request, 'employee'):
            if self.list_permission_codes:
                # Check permissions
                if set(self.list_permission_codes).issubset(request.emp_permissions["codes"]):
                    is_valid = True
            else:
                # Allow if `list_permission_codes` is None
                is_valid = True

        return is_valid
