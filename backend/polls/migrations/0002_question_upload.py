# Generated by Django 4.2 on 2023-04-20 09:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="upload",
            field=models.FileField(
                blank=True, null=True, upload_to="uploads/%Y/%m/%d/"
            ),
        ),
    ]
