# Generated by Django 4.2.11 on 2024-04-23 09:27

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0010_alter_user_date_joined"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="date_joined",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="date joined"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=32, verbose_name="first name"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(blank=True, max_length=32, verbose_name="last name"),
        ),
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
                        "^09\\d{9}$", "Enter a valid phone number."
                    )
                ],
                verbose_name="phone number",
            ),
        ),
    ]
