# Generated by Django 5.0.7 on 2024-07-24 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_packages_depart_time_packages_destination_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='depart_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
