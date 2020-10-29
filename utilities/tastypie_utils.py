from tastypie.authentication import SessionAuthentication


class EmployeeAuthentication(SessionAuthentication):
    """
    Django tastypie session authentication for employee user.
    This also includes authorization and sets permissions etc.
    """

    def __init__(self, allowed_access_types=None):
        super().__init__()
        self.allowed_access_types = allowed_access_types

    def is_authenticated(self, request, **kwargs):
        return (request.user.is_authenticated and hasattr(request, 'employee'))
