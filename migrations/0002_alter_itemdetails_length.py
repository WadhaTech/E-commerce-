# Generated by Django 4.2.10 on 2024-03-06 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Plants", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itemdetails",
            name="length",
            field=models.CharField(max_length=10),
        ),
    ]
