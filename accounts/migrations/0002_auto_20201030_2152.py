# Generated by Django 3.1.2 on 2020-10-30 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('employee_id',), 'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
    ]
