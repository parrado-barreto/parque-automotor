# Generated by Django 4.2.2 on 2023-07-14 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0023_rename_preoperacionalesm_preoperacionalesmotos_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Preoperacionalesmotos',
            new_name='Preoperacionalesm',
        ),
        migrations.AlterModelTable(
            name='preoperacionalesm',
            table='preoperacionalesm',
        ),
    ]