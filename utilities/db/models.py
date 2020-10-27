from django.db import models
from django.utils import timezone


class BaseModelMixin(models.Model):
    """
    Abstract model class to define fundamental fields of a model.
    Inherit from this class to define your models.
    """

    class Meta:
        abstract = True

    created_on = models.DateTimeField(auto_now_add=True, editable=False, help_text='Timestamp at which this record was created.')
    modified_on = models.DateTimeField(auto_now_add=True, editable=False, help_text='Timestamp at which this record was last modified.')


    def clean(self):
        if self.pk:
            self.modified_on = timezone.now()

    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)