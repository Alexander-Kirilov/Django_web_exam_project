# Generated by Django 4.1.2 on 2022-12-17 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction_name', models.CharField(max_length=50)),
                ('instruction_text', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
