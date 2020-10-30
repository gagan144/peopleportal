from django import forms

from conference.models import ConferenceRoom


class ConferenceRoomForm(forms.ModelForm):
    """
    Form to create/edit a Room.
    """

    class Meta:
        model = ConferenceRoom
        fields = ['room_id', 'name', 'booking_email', 'sitting_capacity']

    def save(self, commit=True):
        super(self.__class__, self).save(commit=commit)