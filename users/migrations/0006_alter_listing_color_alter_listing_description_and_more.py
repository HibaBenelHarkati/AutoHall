# Generated by Django 5.1.3 on 2024-11-21 18:37

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_listing_brand_listing_color_listing_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='color',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='engine',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(upload_to=users.models.user_directory_path),
        ),
    ]
