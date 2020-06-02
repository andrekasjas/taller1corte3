# Generated by Django 3.0.6 on 2020-05-31 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desarrollador', '0002_desarrollador_des_pai_id'),
        ('clasificacion', '0001_initial'),
        ('juego', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='jue_cla_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clasificacion.Clasificacion'),
        ),
        migrations.AddField(
            model_name='juego',
            name='jue_des_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='desarrollador.Desarrollador'),
        ),
    ]