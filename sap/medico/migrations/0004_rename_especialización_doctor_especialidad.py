# Generated by Django 4.2.7 on 2023-11-25 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0003_remove_doctor_especializacion_doctor_especialización'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='especialización',
            new_name='especialidad',
        ),
    ]
