from django.shortcuts import render


from peopleportal.decorators import employee_login_required
from conference.models import ConferenceRoom
from conference.forms import ConferenceRoomForm
from utilities.api_utils import ApiResponse



# ----- Room CRUD -----

@employee_login_required(allowed_permission_codes=['conf_room_delete'])
def api_room_delete(request):
    """
    API to delete a room.
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


@employee_login_required(allowed_permission_codes=['conf_room_create'])
def api_room_create(request):
    """
    API to to create a room.
    """

    if request.method.lower() == 'post':

        data = request.POST.dict()
        formRoom = ConferenceRoomForm(data=data)

        if formRoom.is_valid():
            formRoom.save()
            new_room = formRoom.instance
            return ApiResponse.http(status=ApiResponse.ST_SUCCESS, message='New Room successfully created!', room_id=new_room.id)
        else:
            errors = dict(formRoom.errors)
            return ApiResponse.http(status=ApiResponse.ST_FAILED, message='Validation errors.', errors=errors)
    else:
        return ApiResponse.http(status=ApiResponse.ST_FORBIDDEN, message='Use Post!')


@employee_login_required(allowed_permission_codes=['conf_room_edit'])
def api_room_edit(request):
    """
    API to to edit a room.
    """

    if request.method.lower() == 'post':

        data = request.POST.dict()
        room_id = int(request.POST['id'])

        try:
            room = ConferenceRoom.objects.get(id=room_id)

            formRoom = ConferenceRoomForm(data=data, instance=room)

            if formRoom.is_valid():
                formRoom.save()
                return ApiResponse.http(status=ApiResponse.ST_SUCCESS, message='Room successfully updated!', room_id=room_id)
            else:
                errors = dict(formRoom.errors)
                return ApiResponse.http(status=ApiResponse.ST_FAILED, message='Validation errors.', errors=errors)
        except ConferenceRoom.DoesNotExist:
            return ApiResponse.http(status=ApiResponse.ST_FAILED, message='Invalid room.')
    else:
        return ApiResponse.http(status=ApiResponse.ST_FORBIDDEN, message='Use Post!')

# ----- /Room CRUD -----