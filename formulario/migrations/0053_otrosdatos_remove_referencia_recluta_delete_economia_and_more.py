# Generated by Django 5.2.1 on 2025-05-27 12:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("formulario", "0052_situacionjuridica_delete_experiencialaboral"),
    ]

    operations = [
        migrations.CreateModel(
            name="OtrosDatos",
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
                (
                    "fecha_viaje_1",
                    models.DateField(
                        blank=True, null=True, verbose_name="Fecha Viaje 1"
                    ),
                ),
                (
                    "pais_visitado_1",
                    models.CharField(
                        blank=True,
                        max_length=333,
                        null=True,
                        verbose_name="País Visitado 1",
                    ),
                ),
                (
                    "motivo_1",
                    models.CharField(
                        blank=True,
                        max_length=333,
                        null=True,
                        verbose_name="Motivo del viaje 1",
                    ),
                ),
                (
                    "permanencia_1",
                    models.CharField(
                        blank=True,
                        max_length=333,
                        null=True,
                        verbose_name="Tiempo de permanencia 1",
                    ),
                ),
                (
                    "fecha_viaje_2",
                    models.DateField(
                        blank=True, null=True, verbose_name="Fecha Viaje 2"
                    ),
                ),
                (
                    "pais_visitado_2",
                    models.CharField(
                        blank=True,
                        max_length=333,
                        null=True,
                        verbose_name="País Visitado 2",
                    ),
                ),
                (
                    "motivo_2",
                    models.CharField(
                        blank=True,
                        max_length=333,
                        null=True,
                        verbose_name="Motivo del viaje 2",
                    ),
                ),
                (
                    "permanencia_2",
                    models.CharField(
                        blank=True,
                        max_length=333,
                        null=True,
                        verbose_name="Tiempo de permanencia 2",
                    ),
                ),
                (
                    "fecha_viaje_3",
                    models.DateField(
                        blank=True, null=True, verbose_name="Fecha Viaje 3"
                    ),
                ),
                (
                    "pais_visitado_3",
                    models.CharField(
                        blank=True,
                        max_length=333,
                        null=True,
                        verbose_name="País Visitado 3",
                    ),
                ),
                (
                    "motivo_3",
                    models.CharField(
                        blank=True,
                        max_length=333,
                        null=True,
                        verbose_name="Motivo del viaje 3",
                    ),
                ),
                (
                    "permanencia_3",
                    models.CharField(
                        blank=True,
                        max_length=333,
                        null=True,
                        verbose_name="Tiempo de permanencia 3",
                    ),
                ),
                (
                    "recomendante",
                    models.CharField(
                        blank=True,
                        max_length=333,
                        null=True,
                        verbose_name="Por quién tuvo conocimiento de este empleo?",
                    ),
                ),
                (
                    "celular_recomendante",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(100000),
                            django.core.validators.MaxValueValidator(999999999999),
                        ],
                        verbose_name="Celular de quien recomendó",
                    ),
                ),
                (
                    "labora_en_indumil",
                    models.CharField(
                        blank=True,
                        choices=[("Sí", "Sí"), ("No", "No")],
                        null=True,
                        verbose_name="Lo recomienda alguien que labora en la empresa?",
                    ),
                ),
                (
                    "nombres_y_apellidos_recomendante_1",
                    models.CharField(
                        blank=True,
                        max_length=333,
                        null=True,
                        verbose_name="Nombres y apellidos 1",
                    ),
                ),
                (
                    "nombres_y_apellidos_recomendante_2",
                    models.CharField(
                        blank=True,
                        max_length=333,
                        null=True,
                        verbose_name="Nombres y apellidos 2",
                    ),
                ),
                (
                    "cargo_recomendante_1",
                    models.CharField(
                        blank=True,
                        max_length=333,
                        null=True,
                        verbose_name="Cargo Recomendante 1",
                    ),
                ),
                (
                    "cargo_recomendante_2",
                    models.CharField(
                        blank=True,
                        max_length=333,
                        null=True,
                        verbose_name="Cargo Recomendante 2",
                    ),
                ),
                (
                    "unidad_negocio_recomendante_1",
                    models.CharField(
                        blank=True,
                        max_length=333,
                        null=True,
                        verbose_name="Unidad de Negocio Recomendante 1",
                    ),
                ),
                (
                    "unidad_negocio_recomendante_2",
                    models.CharField(
                        blank=True,
                        max_length=333,
                        null=True,
                        verbose_name="Unidad de Negocio Recomendante 2",
                    ),
                ),
                (
                    "tipo_via_recomendante",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Anillo Vial", "Anillo Vial"),
                            ("Autopista", "Autopista"),
                            ("Avenida", "Avenida"),
                            ("Avenida Calle", "Avenida Calle"),
                            ("Avenida Carrera", "Avenida Carrera"),
                            ("Calle", "Calle"),
                            ("Callejón", "Callejón"),
                            ("Carrera", "Carrera"),
                            ("Circular", "Circular"),
                            ("Diagonal", "Diagonal"),
                            ("Transversal", "Transversal"),
                        ],
                        max_length=20,
                        null=True,
                        verbose_name="Tipo de vía",
                    ),
                ),
                (
                    "numero_principal_recomendante",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="Número"
                    ),
                ),
                (
                    "letra_principal_recomendante",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("A", "A"),
                            ("B", "B"),
                            ("C", "C"),
                            ("D", "D"),
                            ("E", "E"),
                            ("F", "F"),
                            ("G", "G"),
                            ("H", "H"),
                            ("I", "I"),
                            ("J", "J"),
                            ("K", "K"),
                            ("L", "L"),
                            ("M", "M"),
                            ("N", "N"),
                            ("O", "O"),
                            ("P", "P"),
                            ("Q", "Q"),
                            ("R", "R"),
                            ("S", "S"),
                            ("T", "T"),
                            ("U", "U"),
                            ("V", "V"),
                            ("W", "W"),
                            ("X", "X"),
                            ("Y", "Y"),
                            ("Z", "Z"),
                        ],
                        max_length=2,
                        null=True,
                        verbose_name="Letra",
                    ),
                ),
                (
                    "bis_recomendante",
                    models.BooleanField(default=False, verbose_name="¿Bis?"),
                ),
                (
                    "letra_bis_recomendante",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("A", "A"),
                            ("B", "B"),
                            ("C", "C"),
                            ("D", "D"),
                            ("E", "E"),
                            ("F", "F"),
                            ("G", "G"),
                            ("H", "H"),
                            ("I", "I"),
                            ("J", "J"),
                            ("K", "K"),
                            ("L", "L"),
                            ("M", "M"),
                            ("N", "N"),
                            ("O", "O"),
                            ("P", "P"),
                            ("Q", "Q"),
                            ("R", "R"),
                            ("S", "S"),
                            ("T", "T"),
                            ("U", "U"),
                            ("V", "V"),
                            ("W", "W"),
                            ("X", "X"),
                            ("Y", "Y"),
                            ("Z", "Z"),
                        ],
                        max_length=2,
                        null=True,
                        verbose_name="Letra Bis",
                    ),
                ),
                (
                    "cuadrante_recomendante",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("ESTE", "ESTE"),
                            ("OESTE", "OESTE"),
                            ("NORTE", "NORTE"),
                            ("SUR", "SUR"),
                        ],
                        max_length=10,
                        null=True,
                        verbose_name="Cuadrante",
                    ),
                ),
                (
                    "numero_secundario_recomendante",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="Número"
                    ),
                ),
                (
                    "letra_secundaria_recomendante",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("A", "A"),
                            ("B", "B"),
                            ("C", "C"),
                            ("D", "D"),
                            ("E", "E"),
                            ("F", "F"),
                            ("G", "G"),
                            ("H", "H"),
                            ("I", "I"),
                            ("J", "J"),
                            ("K", "K"),
                            ("L", "L"),
                            ("M", "M"),
                            ("N", "N"),
                            ("O", "O"),
                            ("P", "P"),
                            ("Q", "Q"),
                            ("R", "R"),
                            ("S", "S"),
                            ("T", "T"),
                            ("U", "U"),
                            ("V", "V"),
                            ("W", "W"),
                            ("X", "X"),
                            ("Y", "Y"),
                            ("Z", "Z"),
                        ],
                        max_length=2,
                        null=True,
                        verbose_name="Letra",
                    ),
                ),
                (
                    "cuadrante_dos_recomendante",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("ESTE", "ESTE"),
                            ("OESTE", "OESTE"),
                            ("NORTE", "NORTE"),
                            ("SUR", "SUR"),
                        ],
                        max_length=10,
                        null=True,
                        verbose_name="Cuadrante",
                    ),
                ),
                (
                    "nro_recomendante",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        verbose_name="Número Final",
                    ),
                ),
                (
                    "complemento_recomendante",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        verbose_name="Complemento/Dirección especial",
                    ),
                ),
                (
                    "razon_de_vinculo",
                    models.TextField(
                        max_length=1123581321,
                        null=True,
                        verbose_name="Explique brevemente la razón por la cual desea vincularse con la empresa:",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="referencia",
            name="recluta",
        ),
        migrations.DeleteModel(
            name="Economia",
        ),
        migrations.DeleteModel(
            name="Referencia",
        ),
    ]
