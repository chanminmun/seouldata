# Generated by Django 5.1.7 on 2025-03-31 10:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("main", "0002_delete_kidtable"),
    ]

    operations = [
        migrations.CreateModel(
            name="tourist_street_table",
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
                ("검색키워드", models.TextField(blank=True, null=True)),
                ("alias", models.TextField(blank=True, null=True)),
                ("최종표기명", models.TextField(blank=True, null=True)),
                ("지번주소", models.TextField(blank=True, null=True)),
                ("행정시", models.TextField(blank=True, null=True)),
                ("행정구", models.TextField(blank=True, null=True)),
                ("행정동", models.TextField(blank=True, null=True)),
                ("키", models.FloatField(blank=True, null=True)),
            ],
            options={
                "db_table": "tourist_street_table",
                "managed": False,
            },
        ),
    ]
