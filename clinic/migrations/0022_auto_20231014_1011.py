# Generated by Django 3.2.15 on 2023-10-14 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0021_auto_20231011_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='reception',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic.reception'),
        ),
        migrations.DeleteModel(
            name='UserReception',
        ),
    ]
