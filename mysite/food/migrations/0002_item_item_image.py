# Generated by Django 5.0.1 on 2024-01-14 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="item_image",
            field=models.CharField(
                default="https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg",
                max_length=500,
            ),
        ),
    ]