from django.db import models

from utilities.db.models import BaseModelMixin


class ConferenceRoom(BaseModelMixin):
    """
    Model to store and manage conference rooms.
    """

    # Enums
    ST_BOOKED = 'booked'
    ST_AVAILABLE = 'available'
    CH_STATUS = (
        (ST_BOOKED, 'Booked'),
        (ST_AVAILABLE, 'Available')
    )

    # Fields
    room_id     = models.CharField(max_length=128, unique=True, db_index=True, help_text='Unique room id.')
    name        = models.CharField(max_length=255, unique=True, help_text='Name of the room.')
    booking_email = models.EmailField(help_text='Booking email-id.')
    sitting_capacity = models.PositiveSmallIntegerField(help_text='Capacity of the conference room.')

    status      = models.CharField(max_length=32, choices=CH_STATUS, default=ST_AVAILABLE, db_index=True, help_text='Current status of the room')

    class Meta:
        ordering = ('room_id',)

    def __str__(self):
        return self.name
