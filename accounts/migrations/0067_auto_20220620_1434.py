# Generated by Django 3.2.13 on 2022-06-20 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0066_auto_20220620_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_update_start',
            name='cause_of_delay',
            field=models.CharField(choices=[('A/W SPARE', 'A/W SPARE'), ('A/W FACILITY', 'A/W FACILITY'), ('A/W OTHER JOB', 'A/W OTHER JOB'), ('OTH', 'OTH'), ('AWAIT UNIT ACCEPT', 'AWAIT UNIT ACCEPT'), ('MULTIPLE FAULTS', 'MULTIPLE FAULTS')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='job_update_start',
            name='job_update_id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='job_update_start',
            name='start_date_actual',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='job_update_start',
            name='start_date_input',
            field=models.DateTimeField(null=True),
        ),
    ]
