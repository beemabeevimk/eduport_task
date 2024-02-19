# Generated by Django 5.0.1 on 2024-02-17 03:33

import accounts.utils
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('vehicle_type', models.PositiveIntegerField(choices=[(accounts.utils.VehicleTypes['TWO_WHEELER'], 'Two wheeler'), (accounts.utils.VehicleTypes['FOUR_WHEELER'], 'Four wheeler')], default=accounts.utils.VehicleTypes['TWO_WHEELER'])),
                ('address', models.TextField()),
                ('age', models.IntegerField()),
                ('driver_status', models.CharField(choices=[('REQUESTED', 'Requested'), ('PROCESSING', 'Processing'), ('VERIFIED', 'Verified')], max_length=25)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('avatar', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rider', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]