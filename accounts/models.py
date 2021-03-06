from django.db import models
from django.contrib.auth.models import User

from utilities.db.models import BaseModelMixin


# ---------- Authorization Models ----------
class Permission(BaseModelMixin):
    """
    Model to store all permissions codes.
    """

    # Enums
    RSC_EMPLOYEE = 'employee'
    RSC_ROOM = 'room'
    CH_RESOURCES = (
        (RSC_EMPLOYEE, 'Employee'),
        (RSC_ROOM, 'Room')
    )

    # Fields
    code    = models.CharField(max_length=128, unique=True, db_index=True, help_text='Permission code.')
    name    = models.CharField(max_length=255, help_text='Name of the permission.')
    resource = models.CharField(max_length=64, choices=CH_RESOURCES, db_index=True, help_text='Resource on which this permission is valid.')

    class Meta:
        unique_together = ('resource', 'code')

    def __str__(self):
        return self.name



class Role(BaseModelMixin):
    """
    Model to store roles along with it's set of permissions.
    """

    name    = models.CharField(max_length=128, unique=True, help_text='Name of the role.')
    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name

    def to_json(self):
        permissions = {}

        for perm in self.permissions.all().order_by('resource', 'code'):
            if perm.resource not in permissions:
                permissions[perm.resource] = []

            permissions[perm.resource].append({
                "code": perm.code,
                "name": perm.name
            })

        return {
            "id": self.id,
            "name": self.name,
            "permissions": permissions
        }

# ---------- /Authorization Models ----------


# ---------- Employee Models ----------
class Team(BaseModelMixin):
    """
    Model to store teams
    """

    name    = models.CharField(max_length=32, unique=True, help_text='Name of the team.')
    description = models.TextField(null=True, blank=True, default=None, help_text='Description about this team.')

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }


class Employee(User, BaseModelMixin):
    """
    Model to store employees.
    This model extends django User model creating a one-to-one relationship. Thus, every employee is a system user.
    """

    employee_id = models.CharField(max_length=64, unique=True, db_index=True, help_text='Unique employee code.')
    phone_no    = models.CharField(max_length=32, help_text='Phone number (along with country code) of the employee.')
    team        = models.ForeignKey(Team, on_delete=models.PROTECT, null=True, db_index=True, help_text='Team in which this employee belongs to.')
    position    = models.CharField(max_length=64, help_text='Position/Designation of the employee.')

    role       = models.ForeignKey(Role, on_delete=models.PROTECT, null=True, help_text='Role of this employee.')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ('employee_id',)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

# ---------- /Employee Models ----------
