# Generated by Django 5.1.3 on 2024-11-14 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_remove_eventinformations_teams_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="EvaluationCriterias",
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
                    "criteria_01",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "criteria_02",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "criteria_03",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "criteria_04",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "criteria_05",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "criteria_06",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "criteria_07",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "criteria_08",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "criteria_09",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "criteria_10",
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