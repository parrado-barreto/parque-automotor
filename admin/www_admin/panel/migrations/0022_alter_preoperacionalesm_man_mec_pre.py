# Generated by Django 4.2.2 on 2023-07-13 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0021_preoperacionalesm_man_mec_pre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preoperacionalesm',
            name='man_mec_pre',
            field=models.CharField(max_length=20),
        ),
    ]
