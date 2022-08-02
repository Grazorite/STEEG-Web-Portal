from django.db import models
from django.contrib.auth.models import User

###########################MAINTABLE####################################

class Maintable(models.Model):
    approvals = (
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
        ('Approved', 'Approved'),
    )

    priorities = (
        ('Priority 1', 'Priority 1'),
        ('Priority 2', 'Priority 2'),
        ('Priority 3', 'Priority 3'),
        ('Others', 'Others'),
    )

    work_centres = (
        ('RBS', 'RBS'), ('EM', 'EM'),
        ('GBAD', 'GBAD'), ('RADAR-WS', 'RADAR-WS'),
        ('GIRAFFE', 'GIRAFFE'), ('SF', 'SF'),
        ('RC', 'RC'), ('SPY', 'SPY'),
        ('ENG', 'ENG'), ('ASTER', 'ASTER'),
        ('ICC-PH', 'ICC-PH'), ('PSTAR', 'PSTAR'),
    )
    
    service_order = models.BigIntegerField(db_column='SERVICE_ORDER', primary_key=True)  # Field name made lowercase.
    service_order_user_status = models.CharField(db_column='SERVICE_ORDER_USER_STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    notification_user_status = models.CharField(db_column='NOTIFICATION_USER_STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    priority_text = models.CharField(db_column='PRIORITY_TEXT', max_length=50, blank=True, null=True, )  # Field name made lowercase.
    mat = models.CharField(db_column='MAT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customer_po_number = models.CharField(db_column='CUSTOMER_PO_NUMBER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    initial_po_number = models.CharField(db_column='Initial_PO_Number', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mo_number = models.BigIntegerField(db_column='MO_NUMBER', blank=True, null=True)  # Field name made lowercase.
    equipment_description = models.CharField(db_column='EQUIPMENT_DESCRIPTION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    model_number = models.CharField(db_column='MODEL_NUMBER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    serial_no = models.CharField(db_column='SERIAL_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mal_start = models.DateField(db_column='MAL_START')  # Field name made lowercase.
    required_start_date = models.DateField(db_column='Required_Start_Date')  # Field name made lowercase.
    required_end_date = models.DateField(db_column='Required_End_Date', blank=True, null=True)  # Field name made lowercase.
    reported_fault_long_text = models.CharField(db_column='Reported_Fault_Long_Text', max_length=50, blank=True, null=True)  # Field name made lowercase.
    capacity_hour = models.FloatField(db_column='CAPACITY_HOUR', blank=True, null=True)  # Field name made lowercase.
    enduser = models.CharField(db_column='ENDUSER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    main_work_center = models.CharField(db_column='MAIN_WORK_CENTER', max_length=50, blank=True, null=True, choices = work_centres)  # Field name made lowercase.
    ctat = models.SmallIntegerField(db_column='CTAT', blank=True, null=True)  # Field name made lowercase.
    calculated_ctat = models.CharField(db_column='Calculated_CTAT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approval_status = models.CharField(db_column='APPROVAL_STATUS', max_length=50, default="Pending", choices=approvals)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MainTable'

    def __str__(self):
        return str(self.service_order)

###########################FOR REPORT GENERATION####################################

class Reportgeneration(models.Model):
    service_order = models.BigIntegerField(db_column='SERVICE_ORDER', primary_key=True)  # Field name made lowercase.
    system = models.CharField(db_column='SYSTEM', max_length=50)  # Field name made lowercase.
    mat = models.CharField(db_column='MAT', max_length=50)  # Field name made lowercase.
    priority_text = models.CharField(db_column='PRIORITY_TEXT', max_length=50)  # Field name made lowercase.
    mal_start = models.DateField(db_column='MAL_START')  # Field name made lowercase.
    mal_end = models.DateField(db_column='MAL_END')  # Field name made lowercase.
    ctat = models.SmallIntegerField(db_column='CTAT')  # Field name made lowercase.
    tet = models.SmallIntegerField(db_column='TET')  # Field name made lowercase.
    out_by = models.SmallIntegerField(db_column='Out_By')  # Field name made lowercase.
    atat = models.SmallIntegerField(db_column='ATAT')  # Field name made lowercase.
    a_w_spare = models.SmallIntegerField(db_column='A_W_SPARE', blank=True, null=True)  # Field name made lowercase.
    a_w_facility = models.CharField(db_column='A_W_FACILITY', max_length=1, blank=True, null=True)  # Field name made lowercase.
    a_w_other_job = models.CharField(db_column='A_W_OTHER_JOB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    inst = models.SmallIntegerField(db_column='INST', blank=True, null=True)  # Field name made lowercase.
    oth = models.SmallIntegerField(db_column='OTH', blank=True, null=True)  # Field name made lowercase.
    await_unit_accept = models.CharField(db_column='AWAIT_UNIT_ACCEPT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    multiple_faults = models.CharField(db_column='MULTIPLE_FAULTS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='REMARKS', max_length=300, blank=True, null=True)  # Field name made lowercase.
    equipment_description = models.CharField(db_column='EQUIPMENT_DESCRIPTION', max_length=50)  # Field name made lowercase.
    model_number = models.CharField(db_column='MODEL_NUMBER', max_length=50)  # Field name made lowercase.
    serial_no = models.CharField(db_column='SERIAL_NO', max_length=50)  # Field name made lowercase.
    reported_fault_long_text = models.CharField(db_column='Reported_Fault_Long_Text', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportGeneration'

    def __str__(self):
        return str(self.service_order)

###########################FOR JOB UPDATE FUNCTIONALITY####################################

class Jobupdatecomplete(models.Model):
    service_order = models.ForeignKey(Maintable, models.DO_NOTHING, db_column='SERVICE_ORDER')  # Field name made lowercase.
    job_complete_id = models.SmallIntegerField(primary_key=True)
    mal_end_date = models.DateField()
    job_complete_input = models.DateField()

    class Meta:
        managed = False
        db_table = 'jobUpdateComplete'

    def __str__(self):
        return str(self.service_order)


class Jobupdateend(models.Model):
    delays = (
        ('A/W SPARE', 'A/W SPARE'),
        ('A/W FACILITY', 'A/W FACILITY'),
        ('A/W OTHER JOB', 'A/W OTHER JOB'),
        ('OTH', 'OTH'),
        ('AWAIT UNIT ACCEPT', 'AWAIT UNIT ACCEPT'),
        ('MULTIPLE FAULTS', 'MULTIPLE FAULTS'),
    )
    service_order = models.ForeignKey(Maintable, models.DO_NOTHING, db_column='SERVICE_ORDER')  # Field name made lowercase.
    job_update = models.OneToOneField('Jobupdatestart', models.DO_NOTHING, db_column='Job_update_id', primary_key=True)  # Field name made lowercase.
    end_date_actual = models.DateField()
    end_date_input = models.DateField()
    cause_of_delay = models.CharField(db_column='Cause_of_Delay', max_length=50, choices = delays)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jobUpdateEnd'
    
    def __str__(self):
        return str(self.job_update)


class Jobupdatestart(models.Model):
    service_order = models.ForeignKey(Maintable, models.DO_NOTHING, db_column='SERVICE_ORDER')  # Field name made lowercase.
    job_update_id = models.SmallIntegerField(db_column='Job_update_id', primary_key=True)  # Field name made lowercase.
    start_date_actual = models.DateField()
    start_date_input = models.DateField()

    class Meta:
        managed = False
        db_table = 'jobUpdateStart'
    
    def __str__(self):
        return str(self.job_update_id)

###########################FOR ASSOCIATED TABLES####################################

class discrepancy_report(models.Model):
    cause_of_delay = (
        ('Parts Missing', 'Parts Missing'),
        ('Equipment Faulty', 'Equipment Faulty'),
        ('To be assessed for OEM repair', 'To be assessed for OEM repair'),
        ('Pending further evaluation', 'Pending further evaluation'),
        ('Priority given to others', 'Priority given to others'),
    )
    discrepancy_id = models.CharField(max_length=200, primary_key=True)
    service_order = models.ForeignKey(Maintable, null=True, on_delete=models.SET_NULL)
    cause_of_delay = models.CharField(max_length=200, null=True, choices=cause_of_delay)
    discrepancy_creation_date = models.DateField(null=True)
    expected_delay_duration = models.IntegerField()

    def __str__(self):
        return self.discrepancy_id


class approval_for_work(models.Model):
    AFW_id = models.IntegerField(primary_key=True)
    service_order = models.ForeignKey(Maintable, null=True, on_delete=models.SET_NULL)
    discrepancy_id = models.ForeignKey(discrepancy_report, null=True, on_delete=models.SET_NULL)
    approval_creation_date = models.DateField(null=True)
    AFW_status = models.BooleanField(default = False)

    def __str__(self):
        return str(self.AFW_id)