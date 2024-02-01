# Generated by Django 5.0.1 on 2024-02-01 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.CharField(max_length=100, verbose_name='ID пользователя')),
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='Никнейм пользователя')),
                ('fullname', models.CharField(blank=True, max_length=100, null=True, verbose_name='Никнейм пользователя')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
            ],
            options={
                'verbose_name': 'Пользователь телеграмма',
                'verbose_name_plural': 'Пользователи телеграмма',
            },
        ),
    ]
