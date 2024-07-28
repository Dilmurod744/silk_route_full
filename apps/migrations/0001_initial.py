# Generated by Django 5.0.7 on 2024-07-24 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/package_images')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('days', models.IntegerField()),
            ],
        ),
    ]
