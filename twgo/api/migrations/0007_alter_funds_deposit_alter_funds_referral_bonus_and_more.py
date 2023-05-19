# Generated by Django 4.2 on 2023-05-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0006_funds"),
    ]

    operations = [
        migrations.AlterField(
            model_name="funds",
            name="deposit",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="funds",
            name="referral_bonus",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="funds",
            name="total_balance",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]