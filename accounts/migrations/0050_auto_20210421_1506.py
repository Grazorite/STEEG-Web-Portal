# Generated by Django 3.0.6 on 2021-04-21 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0049_auto_20210417_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbreport',
            name='report_number',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fbreport',
            name='score',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nonfbreport',
            name='report_number',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nonfbreport',
            name='score',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
