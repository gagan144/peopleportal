from django import forms

from accounts.models import Employee


class EmployeeForm(forms.ModelForm):
    """
    Form ro edit/create an Employee.
    """

    class Meta:
        model = Employee
        fields = ['first_name', 'employee_id', 'email', 'phone_no', 'team', 'position', 'role']

    def save(self, commit=True):
        super(self.__class__, self).save(commit=commit)