# Generated by Django 4.2.7 on 2023-11-26 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0008_remove_cita_doctor_remove_cita_paciente_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='medico.doctor'),
        ),
        migrations.AddField(
            model_name='cita',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='medico.paciente'),
        ),
    ]
