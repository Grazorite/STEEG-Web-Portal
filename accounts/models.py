from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class NonFBChecklist(models.Model):
    checklist_item = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # not sure if we actually need this, can remove later
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.checklist_item


class CovidComplianceChecklist(models.Model):
    measures_item = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # not sure if we actually need this, can remove later
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.measures_item


class FBChecklist(models.Model):
    item = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # not sure if we actually need this, can remove later
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.item

# used as template for Create Report form

class Store(models.Model):
    CATEGORY = (
        ('FB', 'FB'),
        ('Non-FB', 'Non-FB')
    )

    system_name = models.CharField(max_length=200, null=True)
    system_id = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    jobPriority = models.BooleanField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    job_description = models.CharField(max_length=200, null=True, blank=True)
    # to be calculated
    score = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    audit_date = models.DateField("dd/mm/yyyy", auto_now_add=False, null=True)
    # not sure if we actually need this, can remove later
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name


class NonFBReport(models.Model):
    store = models.ForeignKey(Store, null=True, on_delete=models.SET_NULL)
    report_number = models.IntegerField()
    compliance = models.ManyToManyField(NonFBChecklist)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    score = models.IntegerField()

    def __str__(self):
        return str(self.report_number)  # give name in the admin panel


class FBReport(models.Model):
    store = models.ForeignKey(Store, null=True, on_delete=models.SET_NULL)
    report_number = models.IntegerField()
    compliance = models.ManyToManyField(FBChecklist)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    score = models.IntegerField()

    def __str__(self):
        return str(self.report_number)  # give name in the admin panel


class CovidReport(models.Model):
    store = models.ForeignKey(Store, null=True, on_delete=models.SET_NULL)
    report_number = models.IntegerField()
    compliance = models.ManyToManyField(CovidComplianceChecklist)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    score = models.IntegerField()

    def __str__(self):
        return str(self.report_number)  # give name in the admin panel

class Order(models.Model):
    STATUS = (
        ('Notification Sent', 'Notification Sent'),
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )

    store = models.ForeignKey(Store, null=True, on_delete=models.SET_NULL)
    Non_FB_Report = models.ForeignKey(
        NonFBReport, null=True, on_delete=models.SET_NULL)
    FB_Report = models.ForeignKey(
        FBReport, null=True, on_delete=models.SET_NULL)
    Covid_Compliance_Report = models.ForeignKey(
        CovidReport, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    issue = models.ForeignKey(
        NonFBChecklist, null=True, on_delete=models.SET_NULL)
    # if (store.Store):
    #     issue = models.ForeignKey(NonFBChecklist, null=True, on_delete=models.SET_NULL)
    # else:
    #     issue = models.ForeignKey(FBChecklist, null=True, on_delete=models.SET_NULL)
    covid_compliance = models.ForeignKey(
        CovidComplianceChecklist, null=True, on_delete=models.SET_NULL)

    upload_image = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.store.name


class Announcement(models.Model):
    announcement_title = models.CharField(max_length=200, null=True)
    announcement_text = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.announcement_title


class AuditScore(models.Model):
    name = models.CharField(max_length=30)
    score = models.FloatField()

    def __str__(self):
        return "{}: {}".format(self.name, self.score)


class Send_email(models.Model):
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.email


class Statistics_page(models.Model):
    statistics_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.statistics_name

class steeg_user(models.Model):
    stakeholderTypes = (
        ('RSAF', 'RSAF'),
        ('DSTA', 'DSTA'),
        ('Workshop Manager', 'Workshop Manager'),
        ('Workshop Engineer', 'Workshop Engineer'),
    )
    employment_id = models.CharField(max_length=200, primary_key=True)
    user_name = models.CharField(max_length=200, null=True)
    contact_number = models.CharField(max_length=200, null=True)
    stakeholder_type = models.CharField(max_length=200, null=True, choices=stakeholderTypes)
    
    def __str__(self):
        return self.employment_id

class MainDB(models.Model):
    service_ord = models.BigIntegerField(db_column='SERVICE_ORD', primary_key=True)  # Field name made lowercase.
    service_order_user_status = models.CharField(db_column='SERVICE_ORDER_USER_STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    notification_user_status = models.CharField(db_column='NOTIFICATION_USER_STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    priority = models.CharField(db_column='Priority', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mat = models.CharField(db_column='MAT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customer_po_number = models.BigIntegerField(db_column='CUSTOMER_PO_NUMBER', blank=True, null=True)  # Field name made lowercase.
    initial_po_number = models.CharField(db_column='Initial_PO_Number', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mo_number = models.BigIntegerField(db_column='MO_NUMBER', blank=True, null=True)  # Field name made lowercase.
    equipment_description = models.CharField(db_column='EQUIPMENT_DESCRIPTION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    model_number = models.FloatField(db_column='MODEL_NUMBER', blank=True, null=True)  # Field name made lowercase.
    date_in = models.DateField(db_column='DATE_IN', blank=True, null=True)  # Field name made lowercase.
    required_start_date = models.DateField(db_column='Required_Start_Date', blank=True, null=True)  # Field name made lowercase.
    required_end_date = models.DateField(db_column='Required_End_Date', blank=True, null=True)  # Field name made lowercase.
    reported_fault_long_text = models.TextField(db_column='Reported_Fault_Long_Text', blank=True, null=True)  # Field name made lowercase.
    capacity_hour = models.FloatField(db_column='CAPACITY_HOUR', blank=True, null=True)  # Field name made lowercase.
    enduser = models.CharField(db_column='ENDUSER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    main_work_center = models.CharField(db_column='MAIN_WORK_CENTER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctat = models.SmallIntegerField(db_column='CTAT', blank=True, null=True)  # Field name made lowercase.
    calculated_ctat = models.CharField(db_column='Calculated_CTAT', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MainTable'
    
    def __str__(self):
        return str(self.service_ord)


class Jobupdatestart(models.Model):
    service_ord = models.ForeignKey(MainDB, models.DO_NOTHING, db_column='SERVICE_ORD')  # Field name made lowercase.
    job_update_id = models.SmallIntegerField(primary_key=True)
    start_date_actual = models.DateField()
    start_date_input = models.DateField()

    class Meta:
        managed = False
        db_table = 'jobUpdateStart'

    def __str__(self):
        return str(self.job_update_id)

class Jobupdateend(models.Model):
    delays = (
        ('A/W SPARE', 'A/W SPARE'),
        ('A/W FACILITY', 'A/W FACILITY'),
        ('A/W OTHER JOB', 'A/W OTHER JOB'),
        ('OTH', 'OTH'),
        ('AWAIT UNIT ACCEPT', 'AWAIT UNIT ACCEPT'),
        ('MULTIPLE FAULTS', 'MULTIPLE FAULTS'),
    )
    service_order = models.ForeignKey(MainDB, models.DO_NOTHING, db_column='SERVICE_ORDER')  # Field name made lowercase.
    job_update = models.OneToOneField(Jobupdatestart, models.DO_NOTHING, primary_key=True)
    end_date_actual = models.DateField()
    end_date_input = models.DateField()
    cause_of_delay = models.CharField(max_length=200, null=True, choices=delays)

    class Meta:
        managed = False
        db_table = 'jobUpdateEnd'
    
    def __str__(self):
        return str(self.job_update)


class Jobupdatecomplete(models.Model):
    service_order = models.ForeignKey(MainDB, models.DO_NOTHING, db_column='SERVICE_ORDER', blank=True, null=True)  # Field name made lowercase.
    job_update_id = models.SmallIntegerField(primary_key=True)
    mal_end_date = models.DateField(blank=True, null=True)
    job_complete_input = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobUpdateComplete'

    def __str__(self):
        return str(self.job_update_id)

# class JobUpdateStart(models.Model):
#     delays = (
#         ('A/W SPARE', 'A/W SPARE'),
#         ('A/W FACILITY', 'A/W FACILITY'),
#         ('A/W OTHER JOB', 'A/W OTHER JOB'),
#         ('OTH', 'OTH'),
#         ('AWAIT UNIT ACCEPT', 'AWAIT UNIT ACCEPT'),
#         ('MULTIPLE FAULTS', 'MULTIPLE FAULTS'),
#     )
#     service_ord = models.ForeignKey(Ip220610Cleaned, null=True, on_delete=models.SET_NULL)
#     job_update_id = models.BigIntegerField(primary_key=True)
#     cause_of_delay = models.CharField(max_length=200, null=True, choices=delays)
#     start_date_actual = models.DateTimeField(null=True)
#     start_date_input = models.DateTimeField(null=True)

# class JobUpdateEnd(models.Model):
#     service_ord = models.ForeignKey(Ip220610Cleaned, null=True, on_delete=models.SET_NULL)
#     job_update_id = models.OneToOneField(JobUpdateStart, on_delete=models.CASCADE, primary_key=True)
#     end_date_actual = models.DateTimeField(null=True)
#     end_date_input = models.DateTimeField(null=True)

# class JobUpdateComplete(models.Model):
#     service_ord = models.OneToOneField(Ip220610Cleaned, on_delete=models.CASCADE, primary_key=True)
#     mal_end_date = models.DateTimeField(null=True)
#     job_complete_input = models.DateTimeField(null=True)

# class job_status(models.Model):
#     priorities = (
#         ('AOG', 'AOG'),
#         ('P1', 'P1'),
#         ('P2', 'P2'),
#         ('P3', 'P3'),
#         ('NA', 'NA'),
#     )
#     approvalStatus = (
#         ('Pending', 'Pending'),
#         ('Approved', 'Approved'),
#     )
#     service_order_number = models.CharField(max_length=200, primary_key=True)
#     employment_id = models.ForeignKey(steeg_user, null=True, on_delete=models.SET_NULL)
#     approval_status = models.CharField(max_length=200, null=True, choices=approvalStatus)
#     priority = models.CharField(max_length=200, null=True, choices=priorities)

    # def __str__(self):
    #     return self.service_order_number

class equipment_inventory(models.Model):
    serial_number = models.CharField(max_length=200, primary_key=True)
    service_order_number = models.ForeignKey(MainDB, null=True, on_delete=models.SET_NULL)
    system_type = models.CharField(max_length=200, null=True)

class discrepancy_report(models.Model):
    cause_of_delay = (
        ('Parts Missing', 'Parts Missing'),
        ('Equipment Faulty', 'Equipment Faulty'),
        ('To be assessed for OEM repair', 'To be assessed for OEM repair'),
        ('Pending further evaluation', 'Pending further evaluation'),
        ('Priority given to others', 'Priority given to others'),
    )
    discrepancy_id = models.CharField(max_length=200, primary_key=True)
    service_ord = models.ForeignKey(MainDB, null=True, on_delete=models.SET_NULL)
    cause_of_delay = models.CharField(max_length=200, null=True, choices=cause_of_delay)
    discrepancy_creation_date = models.DateField(null=True)
    expected_delay_duration = models.IntegerField()
    def __str__(self):
        return self.discrepancy_id


class approval_for_work(models.Model):
    AFW_id = models.IntegerField(primary_key=True)
    service_ord = models.ForeignKey(MainDB, null=True, on_delete=models.SET_NULL)
    discrepancy_id = models.ForeignKey(discrepancy_report, null=True, on_delete=models.SET_NULL)
    employment_id = models.ForeignKey(steeg_user, null=True, on_delete=models.SET_NULL)
    approval_creation_date = models.DateField(null=True)
    AFW_status = models.BooleanField(default = False) 
    def __str__(self):
        return str(self.AFW_id)