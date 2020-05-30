# Generated by Django 3.0.5 on 2020-05-10 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20200510_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Sex',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='directa',
            field=models.FloatField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='totka',
            field=models.FloatField(blank=True, max_length=20),
        ),
    ]
