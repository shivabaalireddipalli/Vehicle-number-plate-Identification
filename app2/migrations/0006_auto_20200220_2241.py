# Generated by Django 3.0.3 on 2020-02-20 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0005_allvehicle'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AddVehicles',
        ),
        migrations.RenameField(
            model_name='allvehicle',
            old_name='Vehicle_name',
            new_name='Fuel',
        ),
        migrations.AddField(
            model_name='allvehicle',
            name='vname',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='databse',
            name='otp',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
