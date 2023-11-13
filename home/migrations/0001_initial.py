# Generated by Django 4.2.5 on 2023-11-13 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('to', models.CharField(max_length=50)),
                ('free_seats', models.IntegerField(default=0)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user')),
                ('passengers', models.ManyToManyField(related_name='passengers', to='login.user')),
            ],
        ),
    ]
