# Generated by Django 4.1.2 on 2022-12-12 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_photos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photos',
            old_name='tagged_pets',
            new_name='news',
        ),
    ]
