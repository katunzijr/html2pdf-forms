# Generated by Django 5.0.4 on 2024-06-01 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BedNightLevyMaster',
            fields=[
                ('return_id', models.IntegerField(primary_key=True, serialize=False)),
                ('taxpayer_id', models.IntegerField(blank=True, null=True)),
                ('branch_id', models.IntegerField(default=0)),
                ('taxpayer_id_declr', models.IntegerField(blank=True, null=True)),
                ('yearofincome', models.IntegerField()),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
                ('submissiondate', models.DateTimeField(auto_now_add=True)),
                ('category', models.IntegerField(blank=True, db_column='category_id', null=True)),
                ('residential_status', models.CharField(blank=True, max_length=20, null=True)),
                ('entity_type', models.CharField(blank=True, max_length=20, null=True)),
                ('entity_parent_name', models.CharField(blank=True, max_length=256, null=True)),
                ('is_mining', models.CharField(default='N', max_length=1)),
                ('status_ct', models.CharField(blank=True, max_length=30, null=True)),
                ('changeuser', models.CharField(blank=True, max_length=20, null=True)),
                ('changedate', models.DateTimeField(blank=True, null=True)),
                ('change_app_user', models.CharField(blank=True, max_length=20, null=True)),
                ('ip_address', models.CharField(blank=True, max_length=100, null=True)),
                ('err_msg', models.CharField(blank=True, max_length=2000, null=True)),
                ('site', models.BigIntegerField()),
                ('itaxtype_ct', models.CharField(blank=True, max_length=20, null=True)),
                ('period', models.BigIntegerField()),
                ('gfs_code', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('declarant_posn', models.CharField(blank=True, max_length=80, null=True)),
                ('entrydate', models.DateTimeField(auto_now_add=True)),
                ('staff_no', models.CharField(blank=True, max_length=80, null=True)),
                ('duedate', models.DateTimeField(blank=True, null=True)),
                ('assessment_no', models.CharField(blank=True, max_length=20, null=True)),
                ('assess_final_bv', models.CharField(blank=True, max_length=20, null=True)),
                ('net_tax_payable', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('computername', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'BedNightLevyMaster',
                'verbose_name_plural': 'BedNightLevyMasters',
                'db_table': 'EFILE_RET_BNL_MASTER',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='BedNightReturn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_facility', models.PositiveIntegerField()),
                ('attachment', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('return_master', models.ForeignKey(db_column='return_id', on_delete=django.db.models.deletion.CASCADE, related_name='bednights', to='fileupload.bednightlevymaster')),
            ],
            options={
                'verbose_name': 'BedNightReturn',
                'verbose_name_plural': 'BedNightReturns',
                'db_table': 'EFILE_BNL_RETURN',
            },
        ),
    ]
