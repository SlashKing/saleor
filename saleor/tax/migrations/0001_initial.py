# Generated by Django 3.2.6 on 2021-12-17 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TaxCountry",
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
                ("name", models.CharField(max_length=255)),
                ("code", models.CharField(max_length=255)),
                ("tax_rate_name", models.CharField(max_length=255)),
                ("standard_tax_rate", models.PositiveIntegerField(default=23)),
                ("b2b_tax_rate", models.PositiveIntegerField(default=23)),
            ],
        ),
        migrations.CreateModel(
            name="TaxGroup",
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
                ("name", models.CharField(max_length=255)),
                ("code", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="TaxSetting",
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
                ("name", models.CharField(max_length=255)),
                ("include_taxes_in_prices", models.BooleanField(default=False)),
                ("display_gross_prices", models.BooleanField(default=False)),
                ("charge_taxes_on_shipping", models.BooleanField(default=False)),
                ("default", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="TaxCountryRate",
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
                ("value", models.PositiveIntegerField(default=23)),
                (
                    "country",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="country_rates",
                        to="tax.taxcountry",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="country_rates",
                        to="tax.taxgroup",
                    ),
                ),
            ],
        ),
    ]
