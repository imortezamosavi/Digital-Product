# Generated by Django 4.2.11 on 2024-05-05 09:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="device_uuid",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="device uuid"
            ),
        ),
    ]
