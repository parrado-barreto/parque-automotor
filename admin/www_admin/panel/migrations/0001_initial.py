# Generated by Django 4.2.2 on 2023-07-19 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dependencias',
            fields=[
                ('id_dep', models.AutoField(primary_key=True, serialize=False)),
                ('nom_dep', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'dependencias',
            },
        ),
        migrations.CreateModel(
            name='Soat',
            fields=[
                ('id_soa', models.AutoField(primary_key=True, serialize=False)),
                ('nom_emp_soa', models.CharField(max_length=50, null=True)),
                ('fec_exp_soa', models.DateField(null=True)),
                ('fec_ven_soa', models.DateField(null=True)),
            ],
            options={
                'db_table': 'soat',
            },
        ),
        migrations.CreateModel(
            name='Tecnicomecanica',
            fields=[
                ('id_tec', models.AutoField(primary_key=True, serialize=False)),
                ('nom_emp_tec', models.CharField(max_length=50, null=True)),
                ('fec_exp_tec', models.DateField(null=True)),
                ('fec_ven_tec', models.DateField(null=True)),
            ],
            options={
                'db_table': 'tecnicomecanica',
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_per', models.BigIntegerField(primary_key=True, serialize=False)),
                ('pas_per', models.CharField(max_length=30)),
                ('nom_per', models.CharField(max_length=30)),
                ('ape_per', models.CharField(max_length=30)),
                ('tel_per', models.CharField(max_length=30)),
                ('dir_per', models.CharField(max_length=30)),
                ('cat_per', models.CharField(max_length=30)),
                ('vig_per', models.DateField(null=True)),
                ('dep_per', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.dependencias')),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('pla_veh', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('num_lic_veh', models.BigIntegerField()),
                ('cla_veh', models.CharField(max_length=50)),
                ('mar_veh', models.CharField(max_length=50)),
                ('mod_veh', models.IntegerField()),
                ('col_veh', models.CharField(max_length=30)),
                ('num_mot_veh', models.CharField(max_length=50)),
                ('num_cha_veh', models.CharField(max_length=50)),
                ('cil_veh', models.IntegerField()),
                ('tip_car_veh', models.CharField(max_length=50)),
                ('est_veh', models.BooleanField()),
                ('obs_veh', models.CharField(max_length=200, null=True)),
                ('dep_veh', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.dependencias')),
            ],
            options={
                'db_table': 'vehiculos',
            },
        ),
        migrations.CreateModel(
            name='VehiculosAsignados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fec_ing', models.DateTimeField(auto_now_add=True, null=True)),
                ('fec_sal', models.DateTimeField(null=True)),
                ('obs_veh_asi', models.CharField(max_length=200)),
                ('id_per', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='panel.usuarios')),
                ('id_veh', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='panel.vehiculos')),
            ],
            options={
                'db_table': 'vehiculos_asignados',
            },
        ),
        migrations.AddField(
            model_name='vehiculos',
            name='per_asi_veh',
            field=models.ManyToManyField(blank=True, through='panel.VehiculosAsignados', to='panel.usuarios'),
        ),
        migrations.AddField(
            model_name='vehiculos',
            name='soa_veh',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.soat'),
        ),
        migrations.AddField(
            model_name='vehiculos',
            name='tec_veh',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.tecnicomecanica'),
        ),
        migrations.CreateModel(
            name='Preoperacionalesm',
            fields=[
                ('id_pre', models.AutoField(primary_key=True, serialize=False)),
                ('niv_pre', models.CharField(max_length=20)),
                ('man_pre', models.CharField(max_length=20)),
                ('dir_pre', models.CharField(max_length=20)),
                ('gua_pre', models.CharField(max_length=20)),
                ('cha_pre', models.CharField(max_length=20)),
                ('sus_pre', models.CharField(max_length=20)),
                ('fre_pre', models.CharField(max_length=20)),
                ('lla_pre', models.CharField(max_length=20)),
                ('rin_pre', models.CharField(max_length=20)),
                ('tre_pre', models.CharField(max_length=20)),
                ('exo_pre', models.CharField(max_length=20)),
                ('ret_pre', models.CharField(max_length=20)),
                ('man_mec_pre', models.CharField(max_length=20)),
                ('luc_pre', models.CharField(max_length=20)),
                ('dir_stop_pre', models.CharField(max_length=20)),
                ('pit_pre', models.CharField(max_length=20)),
                ('obs_pre', models.CharField(max_length=300)),
                ('pla_pre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.vehiculos')),
            ],
            options={
                'db_table': 'preoperacionalesm',
            },
        ),
    ]
