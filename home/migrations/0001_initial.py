# Generated by Django 4.2.5 on 2023-11-13 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travels2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Travels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('to', models.CharField(max_length=50)),
                ('free_seat', models.IntegerField(default=0)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user')),
            ],
        ),
    ]
