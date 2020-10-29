from tastypie.resources import ModelResource, Resource, ALL, ALL_WITH_RELATIONS, fields

from conference.models import ConferenceRoom
from utilities.tastypie_utils import EmployeeAuthentication


class ConferenceRoomResource(ModelResource):
    """
    Tastypie resource for Conference Room
    """

    class Meta:
        resource_name = 'rooms'
        queryset = ConferenceRoom.objects.all()
        limit = 0
        max_limit = None
        list_allowed_methods = ['get']
        include_resource_uri = False
        authentication = EmployeeAuthentication(list_permission_codes=['conf_room_read'])
