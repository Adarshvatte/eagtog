# Generated by Django 5.0.3 on 2024-04-23 04:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0010_remove_review_product_remove_review_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="image",
            field=models.ImageField(
                default=None, max_length=250, null=True, upload_to="images/"
            ),
        ),
    ]