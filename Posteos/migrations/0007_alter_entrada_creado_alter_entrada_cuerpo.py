# Generated by Django 4.0.5 on 2022-07-25 01:20

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posteos', '0006_alter_entrada_options_remove_entrada_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='creado',
            field=models.DateField(default=datetime.date(2022, 7, 24)),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='cuerpo',
            field=ckeditor.fields.RichTextField(),
        ),
    ]