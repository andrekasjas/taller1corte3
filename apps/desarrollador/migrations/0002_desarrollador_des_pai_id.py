# Generated by Django 3.0.6 on 2020-05-31 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pais', '0002_auto_20200531_1819'),
        ('desarrollador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='desarrollador',
            name='des_pai_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pais.Pais'),
        ),
    ]
