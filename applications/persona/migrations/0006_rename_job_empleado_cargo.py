# Generated by Django 4.2.2 on 2023-06-18 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("persona", "0005_alter_empleado_avatar"),
    ]

    operations = [
        migrations.RenameField(
            model_name="empleado",
            old_name="job",
            new_name="cargo",
        ),
    ]