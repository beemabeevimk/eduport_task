# Generated by Django 5.0.1 on 2024-02-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_driver_status_driver_status_account_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
