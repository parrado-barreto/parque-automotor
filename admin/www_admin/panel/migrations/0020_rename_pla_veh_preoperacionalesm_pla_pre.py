# Generated by Django 4.2.2 on 2023-07-13 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0019_alter_vehiculos_dep_veh_alter_vehiculosasignados_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preoperacionalesm',
            old_name='pla_veh',
            new_name='pla_pre',
        ),
    ]
