# Generated by Django 3.2.15 on 2022-08-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0004_auto_20220828_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(max_length=50, null=True),
        ),
    ]