from django.contrib import admin


class BaseAdminMixin(admin.ModelAdmin):
    list_per_page = 20

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = self.readonly_fields + tuple([field.name for field in self.model._meta.fields if not field.editable])
        return readonly_fields