# Generated by Django 4.1.2 on 2022-12-12 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_newsphotos_alter_news_news_photos_delete_photos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='news_photos',
        ),
    ]
