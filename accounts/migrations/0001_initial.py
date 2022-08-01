# Generated by Django 3.2.13 on 2022-08-01 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobupdatecomplete',
            fields=[
                ('job_complete_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('mal_end_date', models.DateField()),
                ('jobcomplete_input', models.DateField()),
            ],
            options={
                'db_table': 'jobUpdateComplete',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Jobupdatestart',
            fields=[
                ('jobupdateid', models.SmallIntegerField(db_column='Jobupdateid', primary_key=True, serialize=False)),
                ('start_date_actual', models.DateField()),
                ('startdate_input', models.DateField()),
            ],
            options={
                'db_table': 'jobUpdateStart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Maintable',
            fields=[
                ('service_order', models.BigIntegerField(db_column='SERVICE_ORDER', primary_key=True, serialize=False)),
                ('service_order_user_status', models.CharField(blank=True, db_column='SERVICE_ORDER_USER_STATUS', max_length=50, null=True)),
                ('notification_user_status', models.CharField(blank=True, db_column='NOTIFICATION_USER_STATUS', max_length=50, null=True)),
                ('priority', models.CharField(blank=True, db_column='Priority', max_length=50, null=True)),
                ('mat', models.CharField(blank=True, db_column='MAT', max_length=50, null=True)),
                ('customer_po_number', models.BigIntegerField(blank=True, db_column='CUSTOMER_PO_NUMBER', null=True)),
                ('initial_po_number', models.CharField(blank=True, db_column='Initial_PO_Number', max_length=50, null=True)),
                ('mo_number', models.CharField(blank=True, db_column='MO_NUMBER', max_length=50, null=True)),
                ('equipment_description', models.CharField(blank=True, db_column='EQUIPMENT_DESCRIPTION', max_length=50, null=True)),
                ('model_number', models.CharField(blank=True, db_column='MODEL_NUMBER', max_length=50, null=True)),
                ('serial_no', models.CharField(blank=True, db_column='SERIAL_NO', max_length=50, null=True)),
                ('date_in', models.DateField(blank=True, db_column='DATE_IN', null=True)),
                ('required_start_date', models.DateField(blank=True, db_column='Required_Start_Date', null=True)),
                ('required_end_date', models.DateField(blank=True, db_column='Required_End_Date', null=True)),
                ('reported_fault_long_text', models.CharField(blank=True, db_column='Reported_Fault_Long_Text', max_length=50, null=True)),
                ('capacity_hour', models.CharField(blank=True, db_column='CAPACITY_HOUR', max_length=50, null=True)),
                ('enduser', models.CharField(blank=True, db_column='ENDUSER', max_length=50, null=True)),
                ('main_work_center', models.CharField(blank=True, db_column='MAIN_WORK_CENTER', max_length=50, null=True)),
                ('ctat', models.CharField(blank=True, db_column='CTAT', max_length=50, null=True)),
                ('calculated_ctat', models.CharField(blank=True, db_column='Calculated_CTAT', max_length=50, null=True)),
                ('approval_status', models.CharField(blank=True, db_column='APPROVAL_STATUS', default='Pending', max_length=10, null=True)),
            ],
            options={
                'db_table': 'MainTable',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reportgeneration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_order', models.BigIntegerField(db_column='SERVICE_ORDER')),
                ('system', models.CharField(db_column='SYSTEM', max_length=50)),
                ('mat', models.CharField(db_column='MAT', max_length=50)),
                ('priority_text', models.CharField(db_column='PRIORITY_TEXT', max_length=50)),
                ('mal_start', models.DateField(db_column='MAL_START')),
                ('mal_end', models.DateField(db_column='MAL_END')),
                ('ctat', models.SmallIntegerField(db_column='CTAT')),
                ('tet', models.SmallIntegerField(db_column='TET')),
                ('out_by', models.SmallIntegerField(db_column='Out_By')),
                ('atat', models.SmallIntegerField(db_column='ATAT')),
                ('a_w_spare', models.CharField(blank=True, db_column='A_W_SPARE', max_length=1, null=True)),
                ('a_w_facility', models.CharField(blank=True, db_column='A_W_FACILITY', max_length=1, null=True)),
                ('a_w_other_job', models.CharField(blank=True, db_column='A_W_OTHER_JOB', max_length=1, null=True)),
                ('inst', models.SmallIntegerField(db_column='INST')),
                ('oth', models.SmallIntegerField(db_column='OTH')),
                ('await_unit_accept', models.CharField(blank=True, db_column='AWAIT_UNIT_ACCEPT', max_length=1, null=True)),
                ('multiple_faults', models.CharField(blank=True, db_column='MULTIPLE_FAULTS', max_length=1, null=True)),
                ('remarks', models.CharField(db_column='REMARKS', max_length=250)),
                ('equipment_description', models.CharField(db_column='EQUIPMENT_DESCRIPTION', max_length=50)),
                ('model_number', models.CharField(db_column='MODEL_NUMBER', max_length=50)),
                ('serial_no', models.CharField(db_column='SERIAL_NO', max_length=50)),
                ('reported_fault', models.CharField(db_column='REPORTED_FAULT', max_length=50)),
            ],
            options={
                'db_table': 'ReportGeneration',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Jobupdateend',
            fields=[
                ('jobupdateid', models.OneToOneField(db_column='Jobupdateid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='accounts.jobupdatestart')),
                ('end_date_actual', models.DateField()),
                ('enddate_input', models.DateField()),
                ('cause_of_delay', models.CharField(db_column='Cause_of_Delay', max_length=50)),
            ],
            options={
                'db_table': 'jobUpdateEnd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='equipment_inventory',
            fields=[
                ('serial_number', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('system_type', models.CharField(max_length=200, null=True)),
                ('service_order_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.maintable')),
            ],
        ),
        migrations.CreateModel(
            name='discrepancy_report',
            fields=[
                ('discrepancy_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('cause_of_delay', models.CharField(choices=[('Parts Missing', 'Parts Missing'), ('Equipment Faulty', 'Equipment Faulty'), ('To be assessed for OEM repair', 'To be assessed for OEM repair'), ('Pending further evaluation', 'Pending further evaluation'), ('Priority given to others', 'Priority given to others')], max_length=200, null=True)),
                ('discrepancy_creation_date', models.DateField(null=True)),
                ('expected_delay_duration', models.IntegerField()),
                ('service_order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.maintable')),
            ],
        ),
        migrations.CreateModel(
            name='approval_for_work',
            fields=[
                ('AFW_id', models.IntegerField(primary_key=True, serialize=False)),
                ('approval_creation_date', models.DateField(null=True)),
                ('AFW_status', models.BooleanField(default=False)),
                ('discrepancy_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.discrepancy_report')),
                ('service_order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.maintable')),
            ],
        ),
    ]
