from tastypie.resources import ModelResource, Resource, ALL, ALL_WITH_RELATIONS, fields

from accounts.models import Employee
from utilities.tastypie_utils import EmployeeAuthentication


class EmployeeResource(ModelResource):
    """
    Tastypie resource for Employee
    """

    class Meta:
        resource_name = 'employees'
        queryset = Employee.objects.all().select_related('role', 'team')
        limit = 0
        max_limit = None
        list_allowed_methods = ['get']
        include_resource_uri = False
        authentication = EmployeeAuthentication()
        excludes = ['is_staff', 'is_superuser', 'password']


    def dehydrate(self, bundle):
        obj = bundle.obj

        bundle.data['role'] = {
            'id': obj.role.id,
            'name': obj.role.name
        }

        bundle.data['team'] = {
            'id': obj.team.id,
            'name': obj.team.name
        }

        return bundle
