# Generated by Django 5.0.4 on 2024-06-04 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OtherReturnDuedate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATEGORY_ID', models.IntegerField()),
                ('CATEGORY_NAME', models.CharField(max_length=100, null=True)),
                ('DAY', models.IntegerField(null=True)),
                ('MONTH', models.IntegerField()),
                ('YEAR', models.IntegerField()),
                ('DUEDATE', models.DateField()),
                ('IP_ADDRESS', models.CharField(max_length=100, null=True)),
                ('COMPUTERNAME', models.CharField(max_length=100, null=True)),
                ('OS_USER', models.CharField(max_length=100, null=True)),
                ('RATE', models.CharField(max_length=100, null=True)),
                ('ENTRYDATE', models.DateTimeField(auto_now_add=True)),
                ('ENTERED_DATE', models.DateTimeField(auto_now_add=True)),
                ('ENTERED_BY', models.CharField(max_length=100, null=True)),
                ('CHANGED_DATE', models.DateTimeField(auto_now=True)),
                ('CHANGED_BY', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'ReturnDuedate',
                'verbose_name_plural': 'ReturnDuedates',
                'db_table': 'EFILE_T_OTHRETURNS_DUEDATE',
                'ordering': ['-ENTERED_DATE'],
                'unique_together': {('YEAR', 'CATEGORY_ID', 'DUEDATE')},
            },
        ),
        migrations.CreateModel(
            name='UnfiledReturnAnnually',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TAXPAYER_ID', models.BigIntegerField()),
                ('CATEGORY_ID', models.IntegerField()),
                ('CATEGORY_NAME', models.CharField(max_length=100, null=True)),
                ('YEAR', models.IntegerField()),
                ('STATUS', models.IntegerField(choices=[('0', 'Uploaded'), ('1', 'Reviewed'), ('2', 'Approved'), ('3', 'Rejected'), ('4', 'Suspended')], default='0')),
                ('CREATED_AT', models.DateTimeField(auto_now_add=True)),
                ('UPDATED_AT', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'UnfiledReturnAnnually',
                'verbose_name_plural': 'UnfiledReturnAnnuallys',
                'db_table': 'EFILE_UNFILED_RETURN_ANNUALLY',
                'ordering': ['-CREATED_AT'],
                'unique_together': {('TAXPAYER_ID', 'CATEGORY_ID', 'YEAR')},
            },
        ),
        migrations.CreateModel(
            name='UnfiledReturnMonthly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TAXPAYER_ID', models.BigIntegerField()),
                ('CATEGORY_ID', models.IntegerField()),
                ('YEAR', models.IntegerField()),
                ('MONTH', models.IntegerField()),
                ('DUEDATE', models.DateField()),
                ('EXTENDED_DUEDATE', models.DateField(null=True)),
                ('IS_FILLED', models.BooleanField(default=False)),
                ('IS_VISIBLE_TO_TP', models.BooleanField(default=False)),
                ('STATUS', models.IntegerField(choices=[('0', 'Uploaded'), ('1', 'Reviewed'), ('2', 'Approved'), ('3', 'Rejected'), ('4', 'Suspended')], default='0')),
                ('ENTRYDATE', models.DateTimeField(auto_now_add=True)),
                ('UPDATED_AT', models.DateTimeField(auto_now=True)),
                ('UNFILED_ANNUALLY', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='return_annually', to='unfiledreturns.unfiledreturnannually')),
            ],
            options={
                'verbose_name': 'UnfiledReturnMonthly',
                'verbose_name_plural': 'UnfiledReturnMonthlys',
                'db_table': 'EFILE_UNFILED_RETURN_MONTHLY',
                'ordering': ['-ENTRYDATE'],
                'unique_together': {('TAXPAYER_ID', 'CATEGORY_ID', 'DUEDATE')},
            },
        ),
    ]