from django.urls import path, re_path, include

from conference import views
from conference.api import ConferenceRoomResource


api_conferenceRoomResource = ConferenceRoomResource()


urlpatterns = [

    path('room/delete/', views.api_room_delete, name="conference__api_room_delete"),
    path('room/create/', views.api_room_create, name="conference__api_room_create"),
    path('room/edit/', views.api_room_edit, name="conference__api_room_edit"),

    # Api
    re_path(r'^api/', include(api_conferenceRoomResource.urls)),
]