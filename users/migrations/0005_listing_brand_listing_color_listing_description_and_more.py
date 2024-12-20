# Generated by Django 5.1.3 on 2024-11-21 18:35

import django.db.models.deletion
import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='brand',
            field=models.CharField(choices=[('bmw', 'BMW'), ('mercedes benz', 'Mercedes Benz'), ('audi', 'Audi'), ('subaru', 'Subaru'), ('tesla', 'Tesla'), ('jaguar', 'Jaguar'), ('land rover', 'Land Rover'), ('bentley', 'Bentley'), ('bugatti', 'Bugatti'), ('ferrari', 'Ferrari'), ('lamborghini', 'Lamborghini'), ('honda', 'Honda'), ('toyota', 'Toyota'), ('chevrolet', 'Chevrolet'), ('porsche', 'Porsche')], default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='listing',
            name='color',
            field=models.CharField(default='Red', max_length=10),
        ),
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.TextField(default='ici on a la desc'),
        ),
        migrations.AddField(
            model_name='listing',
            name='engine',
            field=models.CharField(default='essence', max_length=20),
        ),
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='media/user/listing/renault-fluence.jpg', upload_to=users.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='listing',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.locations'),
        ),
        migrations.AddField(
            model_name='listing',
            name='transmission',
            field=models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], default=None, max_length=20),
        ),
    ]
