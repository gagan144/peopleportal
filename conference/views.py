from django.shortcuts import render


from conference.models import ConferenceRoom
from peopleportal.decorators import employee_login_required
from utilities.api_utils import ApiResponse


# ----- Room CRUD -----

@employee_login_required(allowed_permission_codes=['conf_room_delete'])
def api_room_delete(request):
    """
    API to delete a rrom.
    """

    if request.method.lower() == 'post':
        room_id = int(request.POST['room_id'])

        try:
            room = ConferenceRoom.objects.get(id=room_id)

            room.delete()

            return ApiResponse.http(status=ApiResponse.ST_SUCCESS, message='Room successfully deleted')

        except ConferenceRoom.DoesNotExist:
            return ApiResponse.http(status=ApiResponse.ST_FAILED, message='Invalid room.')
    else:
        return ApiResponse.http(status=ApiResponse.ST_FORBIDDEN, message='Use Post!')


# ----- /Room CRUD -----