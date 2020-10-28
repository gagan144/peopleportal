from django.core.management.base import BaseCommand
import json
import os
from django.db import transaction


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIR_DATA = os.path.join(BASE_DIR, "data")


class Command(BaseCommand):
    """
    Django admin command to initialize the system.
    This must be run after the system has been perfectly configured and
    all database data has been initialization.

    Command::

        python manage.py initialize_system

    """

    help = "Command to initialize the system. Run this command after the database migration."
    requires_system_checks = True
    can_import_settings = True

    def handle(self, *args, **options):
        from accounts.models import Permission, Role

        self.stdout.write("Initializing system...")
        path_data = os.path.join(DIR_DATA, "data_permissions_roles.json")

        # Read data
        self.stdout.write(f"Reading data file '{path_data}'...")
        with open(path_data, 'r') as f:
            data = json.loads(f.read())

        # Permissions
        self.stdout.write("Upserting 'Permissions' in the database...")
        for perm in data["permissions"]:
            Permission.objects.update_or_create(
                code = perm["code"],
                resource = perm["resource"],
                defaults = {
                    "name": perm["name"]
                }
            )
        self.stdout.write("Done.")


        # Roles
        self.stdout.write("Upserting 'Roles' in the database...")
        for role in data["roles"]:
            with transaction.atomic():
                list_permissions = Permission.objects.filter(code__in=role["permissions"])

                if len(list_permissions) == len(role["permissions"]):
                    role, is_new = Role.objects.get_or_create(name=role["name"])
                    role.permissions.add(*list_permissions)
                else:
                    self.stdout.write(self.style.ERROR("\t[ERROR] Invalid permission(s) in the role '{}'.".format(role["name"])))
        self.stdout.write("Done.")

        # Completed
        self.stdout.write(self.style.SUCCESS('Initialization finished!'))