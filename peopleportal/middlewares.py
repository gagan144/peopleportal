from accounts.models import Employee


class PermissionMiddleware:
    """
    Middleware to set user permissions in the `request` object.
    This middleware checks for currently logged in employee and sets it permissions.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # --- Code to be executed for each request BEFORE the view ---
        user = request.user
        if user.is_authenticated:
            try:
                # Check for employee
                employee = user.employee

                # Set values in the request
                request.employee = employee
                request.emp_permissions = list(employee.role.permissions.all().values_list('code', flat=True))

            except Employee.DoesNotExist:
                pass
        # --- /Before ---

        # Response from the view
        response = self.get_response(request)

        # Code to be executed for each request/response AFTER the view

        return response