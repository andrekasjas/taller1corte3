# Generated by Django 3.0.6 on 2020-05-31 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pai_id', models.IntegerField()),
                ('pai_nom', models.CharField(max_length=60)),
                ('pai_des', models.CharField(max_length=250)),
            ],
        ),
    ]
