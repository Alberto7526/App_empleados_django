# Generated by Django 4.2.2 on 2023-06-18 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("departamentos", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="departamento",
            options={
                "ordering": ["-name"],
                "verbose_name": "Departamento",
                "verbose_name_plural": "Areas de la empresa",
            },
        ),
        migrations.AlterUniqueTogether(
            name="departamento",
            unique_together={("name", "short_name")},
        ),
    ]