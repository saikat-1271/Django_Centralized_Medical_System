# Generated by Django 4.0.6 on 2022-08-09 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_patient_history_doctor_id_patient_history_patient_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient_history',
            name='doctor_id',
        ),
        migrations.RemoveField(
            model_name='patient_history',
            name='patient_id',
        ),
    ]