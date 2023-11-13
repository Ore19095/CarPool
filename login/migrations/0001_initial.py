# Generated by Django 4.2.5 on 2023-11-13 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=8)),
                ('is_passenger', models.BooleanField(default=True)),
                ('asientos_disponibles', models.IntegerField(default=0)),
                ('car_type', models.CharField(default='None', max_length=50)),
                ('car_branch', models.CharField(default='None', max_length=50)),
                ('car_id', models.CharField(default='None', max_length=50)),
                ('car_color', models.CharField(default='None', max_length=50)),
            ],
        ),
    ]
