# Generated by Django 5.0.4 on 2024-04-17 06:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0002_category_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="packing_cost",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="tax",
            field=models.IntegerField(null=True),
        ),
    ]
