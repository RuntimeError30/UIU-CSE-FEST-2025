# Generated by Django 5.1.3 on 2024-11-15 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0019_events_eventdate_events_location_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guidelines",
            name="guideline_pdf",
            field=models.FileField(blank=True, null=True, upload_to="guidelines/"),
        ),
    ]