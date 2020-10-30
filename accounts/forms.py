from django import forms

from accounts.models import Employee


class EmployeeCreateForm(forms.ModelForm):
    """
    Form ro create an Employee.
    """

    class Meta:
        model = Employee
        fields = ['username', 'first_name', 'employee_id', 'email', 'phone_no', 'team', 'position', 'role']

    def save(self, commit=True):
        super(self.__class__, self).save(commit=commit)


class EmployeeEditForm(forms.ModelForm):
    """
    Form ro edit an Employee.
    """

    class Meta:
        model = Employee
        fields = ['first_name', 'employee_id', 'email', 'phone_no', 'team', 'position', 'role']

    def save(self, commit=True):
        super(self.__class__, self).save(commit=commit)