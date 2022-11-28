# Generated by Django 4.1 on 2022-11-28 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Maestro",
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
                ("Nombre", models.CharField(max_length=150)),
                ("ApellidoP", models.CharField(max_length=150)),
                ("ApellidoM", models.CharField(max_length=150)),
                ("Correo", models.CharField(max_length=150)),
                ("Contraseña", models.CharField(max_length=150)),
            ],
        ),
    ]
