# Generated by Django 4.2.2 on 2023-07-27 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_preoperacionalesc'),
    ]

    operations = [
        migrations.AddField(
            model_name='preoperacionalesc',
            name='taco_pre',
            field=models.CharField(default='malo', max_length=20),
        ),
        migrations.AlterField(
            model_name='preoperacionalesc',
            name='obs_pre',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='preoperacionalesm',
            name='obs_pre',
            field=models.CharField(max_length=500),
        ),
    ]