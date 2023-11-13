# Generated by Django 4.2.5 on 2023-11-13 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_user_car_color_user_car_id'),
        ('home', '0002_delete_travels2_rename_person_travels_driver'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travels',
            old_name='free_seat',
            new_name='free_seats',
        ),
        migrations.AddField(
            model_name='travels',
            name='passengers',
            field=models.ManyToManyField(related_name='passengers', to='login.user'),
        ),
    ]