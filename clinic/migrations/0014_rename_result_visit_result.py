# Generated by Django 3.2.15 on 2022-08-30 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0013_auto_20220830_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='Result',
            new_name='result',
        ),
    ]
