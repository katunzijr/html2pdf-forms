# Generated by Django 5.0.4 on 2024-05-02 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LiableToFileReturn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TAXPAYER_ID', models.BigIntegerField(db_column='TAXPAYER_ID')),
                ('CATEGORY_ID', models.IntegerField(db_column='CATEGORY_ID')),
                ('YEAR', models.IntegerField(db_column='YEAR')),
                ('MONTH', models.IntegerField(db_column='MONTH')),
                ('DUEDATE', models.DateField(auto_now_add=True, db_column='DUEDATE')),
                ('EXTENDED_DUEDATE', models.DateField(db_column='EXTENDED_DUEDATE', null=True)),
                ('ENTRYDATE', models.DateField(auto_now_add=True, db_column='ENTRYDATE')),
                ('IS_FILLED', models.BooleanField(default=False)),
                ('IS_VISIBLE_TO_TP', models.BooleanField(default=False)),
                ('STATUS', models.CharField(choices=[('UPD', 'Uploaded'), ('RVD', 'Reviwed'), ('APD', 'Approved')], default='UPD', max_length=3)),
            ],
            options={
                'verbose_name': 'LiableToFileReturn',
                'verbose_name_plural': 'LiableToFileReturns',
                'db_table': 'ITAX.OTHER_RETURN_UNFILED_MONTHLY',
            },
        ),
    ]