# Generated by Django 3.2.15 on 2023-10-11 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0020_auto_20231011_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='reception',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reception', to='clinic.userprofile'),
        ),
        migrations.AlterField(
            model_name='reception',
            name='doctor',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]
