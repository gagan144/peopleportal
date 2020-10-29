from django.urls import path, re_path, include

from conference import views
from conference.api import ConferenceRoomResource


api_conferenceRoomResource = ConferenceRoomResource()


urlpatterns = [

    # Api
    re_path(r'^api/', include(api_conferenceRoomResource.urls)),
]