# Generated by Django 5.1.1 on 2025-06-08 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermodel",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
