# Generated by Django 5.2.1 on 2025-06-13 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("formulario", "0063_remove_datosfamiliares_bis_hermano_1_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="direccionesanteriores",
            name="direccion_completa_anterior_1",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="direccionesanteriores",
            name="direccion_completa_anterior_2",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
