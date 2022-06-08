# Generated by Django 4.0.4 on 2022-06-07 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0053_rename_description_store_job_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='steeg_user',
            fields=[
                ('employment_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=200, null=True)),
                ('contact_number', models.CharField(max_length=200, null=True)),
                ('stakeholder_type', models.CharField(choices=[('RSAF', 'RSAF'), ('DSTA', 'DSTA'), ('Workshop Manager', 'Workshop Manager'), ('Workshop Engineer', 'Workshop Engineer')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='job_status',
            fields=[
                ('service_order_number', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('approval_status', models.CharField(max_length=200, null=True)),
                ('priority', models.CharField(choices=[('AOG', 'AOG'), ('P1', 'P1'), ('P1', 'P1'), ('P1', 'P1'), ('NA', 'NA')], max_length=200, null=True)),
                ('employment_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.steeg_user')),
            ],
        ),
        migrations.CreateModel(
            name='equipment_inventory',
            fields=[
                ('serial_number', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('system_type', models.CharField(max_length=200, null=True)),
                ('service_order_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.job_status')),
            ],
        ),
        migrations.CreateModel(
            name='dicrepancy_report',
            fields=[
                ('discrepancy_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('service_order_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.job_status')),
            ],
        ),
        migrations.CreateModel(
            name='approval_for_work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AFW_status', models.BooleanField(null=True)),
                ('employment_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.steeg_user')),
                ('service_order_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.job_status')),
            ],
        ),
    ]
