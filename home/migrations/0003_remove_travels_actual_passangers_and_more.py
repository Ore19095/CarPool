# Generated by Django 4.2.5 on 2023-11-13 04:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_user_car_branch_user_car_type_user_is_passenger'),
        ('home', '0002_remove_travels_person_travels_actual_passangers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travels',
            name='actual_passangers',
        ),
        migrations.RemoveField(
            model_name='travels',
            name='conductor',
        ),
        migrations.RemoveField(
            model_name='travels',
            name='max_passangers',
        ),
        migrations.RemoveField(
            model_name='travels',
            name='passangers',
        ),
        migrations.AddField(
            model_name='travels',
            name='person',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='login.user'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='passanger',
        ),
    ]
