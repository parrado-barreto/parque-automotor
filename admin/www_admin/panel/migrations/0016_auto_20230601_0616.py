# Generated by Django 3.1.7 on 2023-06-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0015_auto_20230531_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='cat_per',
            field=models.CharField(max_length=30),
        ),
    ]