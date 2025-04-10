# Generated by Django 5.1.7 on 2025-04-09 15:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0014_delete_userprofile"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("username", models.CharField(max_length=150, unique=True)),
                ("password", models.CharField(max_length=128)),
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
