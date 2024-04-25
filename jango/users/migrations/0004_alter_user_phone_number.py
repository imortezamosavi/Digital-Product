# Generated by Django 4.2.11 on 2024-04-22 09:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_user_managers_alter_user_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.BigIntegerField(
                blank=True, null=True, verbose_name="phone number"
            ),
        ),
    ]
