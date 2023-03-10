# Generated by Django 4.1.4 on 2022-12-28 02:07

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    replaces = [
        ("inventory", "0001_initial"),
        ("inventory", "0002_tag_component_tags"),
        ("inventory", "0003_alter_component_tags"),
        ("inventory", "0004_alter_component_tags_alter_tag_name"),
        ("inventory", "0005_component_cost"),
        ("inventory", "0006_component_category"),
        ("inventory", "0007_alter_component_category"),
    ]

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Component",
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
                ("name", models.CharField(max_length=256, unique=True)),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        default=Decimal("0"),
                        max_digits=10,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0"))
                        ],
                    ),
                ),
                ("drop_shipped", models.BooleanField(default=False)),
                ("stock", models.IntegerField(default=0)),
                ("url", models.CharField(blank=True, max_length=1024)),
                ("notes", models.TextField(blank=True)),
                ("about", models.TextField(blank=True)),
                ("metadata", models.JSONField(blank=True, default=dict)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Image",
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
                ("name", models.CharField(blank=True, max_length=128, null=True)),
                ("default", models.BooleanField(default=False)),
                ("file", models.ImageField(upload_to="images/components/")),
                (
                    "component",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="inventory.component",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="component",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="+", to="inventory.tag"
            ),
        ),
        migrations.AddField(
            model_name="component",
            name="cost",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0"),
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(Decimal("0"))],
            ),
        ),
        migrations.AddField(
            model_name="component",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("keyboard", "Keyboard (Complete)"),
                    ("barebones", "Keyboard (Barebones)"),
                    ("switches", "Switches"),
                    ("keycaps", "Keycaps"),
                    ("cable", "Cable"),
                    ("accessory", "Accessory"),
                    ("other", "Other"),
                ],
                max_length=128,
                null=True,
            ),
        ),
    ]
