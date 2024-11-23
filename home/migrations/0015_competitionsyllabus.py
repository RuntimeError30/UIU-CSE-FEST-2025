# Generated by Django 5.1.3 on 2024-11-14 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0014_bonuscriterias"),
    ]

    operations = [
        migrations.CreateModel(
            name="competitionSyllabus",
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
                    "syllabus_01",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "syllabus_02",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "syllabus_03",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "syllabus_04",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "syllabus_05",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "syllabus_06",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "syllabus_07",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "syllabus_08",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "syllabus_09",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "syllabus_10",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.events"
                    ),
                ),
            ],
        ),
    ]