# Generated by Django 5.2.1 on 2025-05-22 16:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("formulario", "0043_informacionacademica"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReferenciasPersonales",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="access_check",
            field=models.CharField(
                choices=[("Sí", "Sí"), ("No", "No")], null=True, verbose_name="Access"
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="año_estudios_1",
            field=models.CharField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1900),
                    django.core.validators.MaxValueValidator(2030),
                ],
                verbose_name="Año",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="año_estudios_2",
            field=models.CharField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1900),
                    django.core.validators.MaxValueValidator(2030),
                ],
                verbose_name="Año",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="año_estudios_3",
            field=models.CharField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1900),
                    django.core.validators.MaxValueValidator(2030),
                ],
                verbose_name="Año",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="año_estudios_4",
            field=models.CharField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1900),
                    django.core.validators.MaxValueValidator(2030),
                ],
                verbose_name="Año",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="ciudad_estudios_1",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Ciudad"
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="ciudad_estudios_2",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Ciudad"
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="ciudad_estudios_3",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Ciudad"
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="ciudad_estudios_4",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Ciudad"
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="escribe_idioma_extranjero_1",
            field=models.CharField(
                blank=True,
                choices=[("Sí", "Sí"), ("No", "No")],
                null=True,
                verbose_name="¿Escribe?",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="escribe_idioma_extranjero_2",
            field=models.CharField(
                blank=True,
                choices=[("Sí", "Sí"), ("No", "No")],
                null=True,
                verbose_name="¿Escribe?",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="estudios_1",
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                verbose_name="Estudios Realizados 1",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="estudios_2",
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                verbose_name="Estudios Realizados 2",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="estudios_3",
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                verbose_name="Estudios Realizados 3",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="estudios_4",
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                verbose_name="Estudios Realizados 4",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="excel_check",
            field=models.CharField(
                choices=[("Sí", "Sí"), ("No", "No")], null=True, verbose_name="Excel"
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="habla_idioma_extranjero_1",
            field=models.CharField(
                blank=True,
                choices=[("Sí", "Sí"), ("No", "No")],
                null=True,
                verbose_name="¿Habla?",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="habla_idioma_extranjero_2",
            field=models.CharField(
                blank=True,
                choices=[("Sí", "Sí"), ("No", "No")],
                null=True,
                verbose_name="¿Escribe?",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="idioma_extranjero_1",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Idioma extranjero 1"
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="idioma_extranjero_2",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Idioma extranjero 2"
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="internet_check",
            field=models.CharField(
                choices=[("Sí", "Sí"), ("No", "No")], null=True, verbose_name="Internet"
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="lee_idioma_extranjero_1",
            field=models.CharField(
                blank=True,
                choices=[("Sí", "Sí"), ("No", "No")],
                null=True,
                verbose_name="¿Lee?",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="lee_idioma_extranjero_2",
            field=models.CharField(
                blank=True,
                choices=[("Sí", "Sí"), ("No", "No")],
                null=True,
                verbose_name="¿Lee?",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="nombre_institucion_estudios_1",
            field=models.CharField(
                blank=True,
                max_length=70,
                null=True,
                verbose_name="Nombre de la Institución",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="nombre_institucion_estudios_2",
            field=models.CharField(
                blank=True,
                max_length=70,
                null=True,
                verbose_name="Nombre de la Institución",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="nombre_institucion_estudios_3",
            field=models.CharField(
                blank=True,
                max_length=70,
                null=True,
                verbose_name="Nombre de la Institución",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="nombre_institucion_estudios_4",
            field=models.CharField(
                blank=True,
                max_length=70,
                null=True,
                verbose_name="Nombre de la Institución",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="otro_check",
            field=models.CharField(
                blank=True,
                max_length=333,
                null=True,
                verbose_name="Otros (Separe por comas)",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="powerpoint_check",
            field=models.CharField(
                choices=[("Sí", "Sí"), ("No", "No")],
                null=True,
                verbose_name="Power Point",
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="titulo_estudios_1",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Título Recibido"
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="titulo_estudios_2",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Título Recibido"
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="titulo_estudios_3",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Título Recibido"
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="titulo_estudios_4",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Título Recibido"
            ),
        ),
        migrations.AddField(
            model_name="informacionacademica",
            name="word_check",
            field=models.CharField(
                choices=[("Sí", "Sí"), ("No", "No")], null=True, verbose_name="Word"
            ),
        ),
        migrations.DeleteModel(
            name="Contacto",
        ),
    ]
