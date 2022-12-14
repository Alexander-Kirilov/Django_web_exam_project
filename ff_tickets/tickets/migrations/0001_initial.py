# Generated by Django 4.1.2 on 2022-12-11 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(choices=[('F01', 'F01'), ('F02', 'F02'), ('F03', 'F03'), ('F04', 'F04'), ('F05', 'F05'), ('F06', 'F06'), ('F07', 'F07'), ('F08', 'F08'), ('F09', 'F09'), ('F10', 'F10')], max_length=10, verbose_name='Обект')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Подал')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновен')),
                ('problem_type', models.CharField(choices=[('scale', 'Везна'), ('cash_place', 'Каса'), ('cash_place_scale', 'Везна - каса'), ('HHT', 'Хенди'), ('other', 'Друго')], default='other', max_length=30, null=True, verbose_name='Вид проблем')),
                ('problem_description', models.TextField(max_length=400, verbose_name='Описание')),
                ('date_of_submit', models.DateTimeField(auto_now_add=True, verbose_name='Дата на подаване')),
                ('problem_status', models.CharField(choices=[('a_posted', 'Подаден'), ('b_confirmed', 'Приет'), ('c_solved', 'Разрешен'), ('d_completed', 'Приключен')], default='a_posted', max_length=50, null=True, verbose_name='Статус')),
                ('comments', models.TextField(blank=True, default='', max_length=800, null=True, verbose_name='Коментар')),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignee_user', to=settings.AUTH_USER_MODEL, verbose_name='Назначен')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['problem_status', 'date_of_submit'],
            },
        ),
    ]