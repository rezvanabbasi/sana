# Generated by Django 3.2.15 on 2023-10-01 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0018_remove_userprofile_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(max_length=30, null=True),
        ),
    ]