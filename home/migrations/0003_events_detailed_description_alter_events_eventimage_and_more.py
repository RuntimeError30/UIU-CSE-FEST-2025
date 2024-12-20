# Generated by Django 5.1.3 on 2024-11-13 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_events_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="events",
            name="detailed_description",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="events",
            name="eventImage",
            field=models.ImageField(blank=True, null=True, upload_to="event_images/"),
        ),
        migrations.CreateModel(
            name="contactInfos",
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
                ("name", models.CharField(max_length=100)),
                ("designation", models.CharField(max_length=200)),
                ("phone_no", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=100)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.events"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="eventRules",
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
                ("Eligibility", models.CharField(max_length=100)),
                ("teams", models.CharField(max_length=100)),
                ("problem_setter", models.CharField(max_length=100)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.events"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="prizeMoney",
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
                ("first_prize", models.CharField(max_length=100)),
                ("second_prize", models.CharField(max_length=100)),
                ("third_prize", models.CharField(max_length=100)),
                ("fourthToTenth_prize", models.CharField(max_length=100)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.events"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="timeLine",
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
                ("timeline_01", models.CharField(max_length=100)),
                ("timeline_02", models.CharField(max_length=100)),
                ("timeline_03", models.CharField(max_length=100)),
                ("timeline_04", models.CharField(max_length=100)),
                ("timeline_05", models.CharField(max_length=100)),
                ("timeline_06", models.CharField(max_length=100)),
                ("timeline_07", models.CharField(max_length=100)),
                ("timeline_08", models.CharField(max_length=100)),
                ("timeline_09", models.CharField(max_length=100)),
                ("timeline_10", models.CharField(max_length=100)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.events"
                    ),
                ),
            ],
        ),
    ]
