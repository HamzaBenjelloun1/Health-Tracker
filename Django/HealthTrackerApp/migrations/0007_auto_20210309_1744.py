# Generated by Django 3.1.5 on 2021-03-09 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthTrackerApp', '0006_auto_20210309_1742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measures',
            old_name='id_patient',
            new_name='rfid_patient',
        ),
    ]