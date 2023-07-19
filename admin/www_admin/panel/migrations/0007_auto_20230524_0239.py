# Generated by Django 3.1.7 on 2023-05-24 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0006_auto_20230524_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependencias',
            name='id_dep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='panel.usuarios'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='dep_per',
            field=models.IntegerField(),
        ),
    ]