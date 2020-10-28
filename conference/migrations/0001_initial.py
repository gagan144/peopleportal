# Generated by Django 3.1.2 on 2020-10-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConferenceRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Timestamp at which this record was created.')),
                ('modified_on', models.DateTimeField(auto_now_add=True, help_text='Timestamp at which this record was last modified.')),
                ('room_id', models.CharField(db_index=True, help_text='Unique room id.', max_length=128, unique=True)),
                ('name', models.CharField(help_text='Name of the room.', max_length=255, unique=True)),
                ('booking_email', models.EmailField(help_text='Booking email-id.', max_length=254)),
                ('sitting_capacity', models.PositiveSmallIntegerField(help_text='Capacity of the conference room.')),
                ('status', models.CharField(choices=[('booked', 'Booked'), ('available', 'Available')], db_index=True, default='available', help_text='Current status of the room', max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]