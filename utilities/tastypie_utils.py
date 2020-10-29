from tastypie.authentication import SessionAuthentication

from accounts.auth import has_authorization


class EmployeeAuthentication(SessionAuthentication):
    """
    Django tastypie session authentication for employee user.
    This also includes authorization and sets permissions etc.
    """

    def __init__(self, allowed_permission_codes=None):
        super().__init__()
        self.allowed_permission_codes = allowed_permission_codes

    def is_authenticated(self, request, **kwargs):
        is_valid = has_authorization(request=request, allowed_permission_codes=self.allowed_permission_codes)
        return is_valid
