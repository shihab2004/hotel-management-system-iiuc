# Generated by Django 5.1.4 on 2024-12-15 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_room_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="hotel",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rooms",
                to="core.hotel",
            ),
        ),
    ]