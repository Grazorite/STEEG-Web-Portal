# Generated by Django 4.0.4 on 2022-06-08 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0054_steeg_user_job_status_equipment_inventory_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='dicrepancy_report',
            new_name='discrepancy_report',
        ),
    ]