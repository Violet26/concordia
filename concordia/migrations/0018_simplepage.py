# Generated by Django 2.0.9 on 2018-11-26 21:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("concordia", "0017_change_transcription_supersedes_related_name")]

    operations = [
        migrations.CreateModel(
            name="SimplePage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "path",
                    models.CharField(
                        help_text="URL path where this page will be accessible from",
                        max_length=255,
                        validators=[django.core.validators.RegexValidator("^/.+/$")],
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("body", models.TextField()),
            ],
        )
    ]
