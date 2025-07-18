# Generated by Django 5.2.1 on 2025-05-27 19:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("formulario", "0054_remove_viajeexterior_recluta_delete_bien_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bienesrentasaep",
            name="arriendos",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(999999999999),
                ],
                verbose_name="Arriendos",
            ),
        ),
        migrations.AlterField(
            model_name="bienesrentasaep",
            name="cesantías_e_intereses_de_cesantías",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(999999999999),
                ],
                verbose_name="Cesantías e intereses de cesantías",
            ),
        ),
        migrations.AlterField(
            model_name="bienesrentasaep",
            name="gastos_de_representación",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(999999999999),
                ],
                verbose_name="Gastos de representación",
            ),
        ),
        migrations.AlterField(
            model_name="bienesrentasaep",
            name="honorarios",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(999999999999),
                ],
                verbose_name="Honorarios",
            ),
        ),
        migrations.AlterField(
            model_name="bienesrentasaep",
            name="otros_ingresos_y_rentas",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(999999999999),
                ],
                verbose_name="Otros ingresos y rentas",
            ),
        ),
        migrations.AlterField(
            model_name="bienesrentasaep",
            name="salarios_y_demas_ingresos_laborales",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(999999999999),
                ],
                verbose_name="Salarios y demás ingresos laborales",
            ),
        ),
        migrations.AlterField(
            model_name="informacionacademica",
            name="año_estudios_1",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1900),
                    django.core.validators.MaxValueValidator(2030),
                ],
                verbose_name="Año",
            ),
        ),
        migrations.AlterField(
            model_name="informacionacademica",
            name="año_estudios_2",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1900),
                    django.core.validators.MaxValueValidator(2030),
                ],
                verbose_name="Año",
            ),
        ),
        migrations.AlterField(
            model_name="informacionacademica",
            name="año_estudios_3",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1900),
                    django.core.validators.MaxValueValidator(2030),
                ],
                verbose_name="Año",
            ),
        ),
        migrations.AlterField(
            model_name="informacionacademica",
            name="año_estudios_4",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1900),
                    django.core.validators.MaxValueValidator(2030),
                ],
                verbose_name="Año",
            ),
        ),
    ]
