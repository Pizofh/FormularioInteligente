# Generated by Django 5.2.1 on 2025-05-29 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("formulario", "0060_remove_datosfamiliares_edad_hijo_1_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datosfamiliares",
            name="recluta",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="formulario.recluta",
            ),
        ),
    ]
