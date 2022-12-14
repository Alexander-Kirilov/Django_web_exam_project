# Generated by Django 4.1.2 on 2022-12-12 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0004_rename_tagged_pets_photos_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='location',
        ),
        migrations.RemoveField(
            model_name='photos',
            name='news',
        ),
        migrations.RemoveField(
            model_name='photos',
            name='user',
        ),
        migrations.AddField(
            model_name='photos',
            name='news',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.RESTRICT, to='news.news'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photos',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
