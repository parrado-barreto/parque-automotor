# Generated by Django 3.1.7 on 2023-05-31 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0013_auto_20230526_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='soat',
            name='nom_emp_soa',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tecnicomecanica',
            name='nom_emp_tec',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculos',
            name='soa_veh',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.soat'),
        ),
        migrations.AlterField(
            model_name='vehiculos',
            name='tec_veh',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.tecnicomecanica'),
        ),
    ]