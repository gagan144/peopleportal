from django.contrib import admin

from conference.models import *
from utilities.db.admin import BaseAdminMixin


@admin.register(ConferenceRoom)
class ConferenceRoomAdmin(BaseAdminMixin):
    list_display = ('room_id', 'name', 'booking_email', 'sitting_capacity', 'status', 'created_on')
    list_filter = ('status', 'created_on')
