# Generated by Django 4.1.4 on 2022-12-28 02:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("inventory", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomBuild",
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
                ("name", models.CharField(default="My Build", max_length=256)),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (0, "Draft"),
                            (1, "Review"),
                            (2, "Finalized"),
                            (-1, "Archived"),
                        ],
                        default=0,
                    ),
                ),
                ("public", models.BooleanField(default=False)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="builds",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "components",
                    models.ManyToManyField(
                        related_name="builds_using", to="inventory.component"
                    ),
                ),
            ],
        ),
    ]
