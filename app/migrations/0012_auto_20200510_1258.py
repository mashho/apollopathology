# Generated by Django 3.0.5 on 2020-05-10 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200510_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='TGlob',
            field=models.FloatField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Talbo',
            field=models.FloatField(blank=True, max_length=20),
        ),
    ]
