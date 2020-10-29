
def has_authorization(request, allowed_permission_codes):
    """
    Method to check if the user has authorization for a request.
    """

    is_valid = False

    # Check user is logged in and is an employee
    if request.user.is_authenticated and hasattr(request, 'employee'):
        if allowed_permission_codes:
            # Check permissions
            if set(allowed_permission_codes).issubset(request.emp_permissions["codes"]):
                is_valid = True
        else:
            # Allow if `list_permission_codes` is None
            is_valid = True

    return is_valid