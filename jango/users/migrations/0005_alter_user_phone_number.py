# Generated by Django 4.2.11 on 2024-04-22 09:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_user_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.BigIntegerField(
                blank=True,
                error_messages={
                    "unique": "A user with this phone number already exists."
                },
                null=True,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^989[0-3,9]\\d{8}$", "Enter a valid phone number."
                    )
                ],
                verbose_name="phone number",
            ),
        ),
    ]
