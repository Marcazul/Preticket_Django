# Generated by Django 4.2.1 on 2023-06-11 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_fecha_primer_servicio_servicio_fecha_servicio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='fecha_servicio',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
