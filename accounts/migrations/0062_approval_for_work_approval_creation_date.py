# Generated by Django 4.0.4 on 2022-06-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0061_remove_approval_for_work_service_order_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='approval_for_work',
            name='approval_creation_date',
            field=models.DateField(null=True),
        ),
    ]
