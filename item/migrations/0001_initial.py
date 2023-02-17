# Generated by Django 4.1.7 on 2023-02-16 20:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=125, unique=True)),
                ("create_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]