# Generated by Django 5.0.1 on 2024-02-17 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_driver_rider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='driver_status',
            new_name='status',
        ),
        migrations.AddField(
            model_name='account',
            name='user_type',
            field=models.CharField(choices=[('DRIVER', 'Driver'), ('RIDER', 'Rider')], default='RIDER', max_length=10),
        ),
    ]