# Generated by Django 5.1.7 on 2025-04-03 14:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_문화공간"),
    ]

    operations = [
        migrations.CreateModel(
            name="야경명소",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("분류", models.TextField(blank=True, null=True)),
                ("장소명", models.TextField(blank=True, null=True)),
                ("주소", models.TextField(blank=True, null=True)),
                ("전화번호", models.TextField(blank=True, null=True)),
                ("홈페이지URL", models.TextField(blank=True, null=True)),
                ("운영시간", models.TextField(blank=True, null=True)),
                ("유무료구분", models.TextField(blank=True, null=True)),
                ("이용요금", models.TextField(blank=True, null=True)),
                ("내용", models.TextField(blank=True, null=True)),
                ("지하철", models.TextField(blank=True, null=True)),
                ("버스", models.TextField(blank=True, null=True)),
                ("주차안내", models.TextField(blank=True, null=True)),
                ("위도", models.FloatField(blank=True, null=True)),
                ("경도", models.FloatField(blank=True, null=True)),
            ],
            options={
                "db_table": "night_table",
                "managed": False,
            },
        ),
    ]
