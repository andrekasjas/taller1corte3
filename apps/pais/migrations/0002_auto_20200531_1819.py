# Generated by Django 3.0.6 on 2020-05-31 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pais', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pais',
            name='id',
        ),
        migrations.AlterField(
            model_name='pais',
            name='pai_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]