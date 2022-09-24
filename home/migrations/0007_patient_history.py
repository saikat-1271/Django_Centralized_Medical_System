# Generated by Django 4.0.6 on 2022-08-09 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_patient_add_patient_bp_patient_case_patient_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=50)),
                ('doctor_id', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('report', models.CharField(max_length=100)),
                ('test_done', models.CharField(max_length=10)),
                ('prescription', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'patient_history',
            },
        ),
    ]