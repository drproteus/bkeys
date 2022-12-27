# Generated by Django 4.1.4 on 2022-12-27 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cable",
            name="input",
            field=models.CharField(
                choices=[
                    ("micro", "Micro USB"),
                    ("mini", "Mini USB"),
                    ("type-c", "USB-C"),
                ],
                default="micro",
                max_length=128,
            ),
        ),
        migrations.AlterField(
            model_name="cable",
            name="output",
            field=models.CharField(
                choices=[("type-a", "USB-A"), ("type-c", "USB-C")],
                default="type-a",
                max_length=128,
            ),
        ),
    ]
