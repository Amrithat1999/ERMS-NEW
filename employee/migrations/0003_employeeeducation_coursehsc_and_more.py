# Generated by Django 4.1.2 on 2023-06-28 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employeeexperience_employeeeducation'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeeducation',
            name='coursehsc',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='percentagehsc',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='schoolhsc',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='yearofpassinghsc',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
