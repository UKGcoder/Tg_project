# Generated by Django 4.1.3 on 2022-11-27 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodicTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='ID пользователя в Телеграмм')),
                ('fun', models.CharField(max_length=20, verbose_name='Название периодической функции')),
                ('job_id', models.CharField(max_length=20, verbose_name='id задачи')),
                ('hour', models.CharField(default='*', max_length=20, verbose_name='В какой час вызвать')),
                ('minute', models.CharField(default='*', max_length=20, verbose_name='В какую минуту вызвать')),
                ('second', models.CharField(default='*', max_length=20, verbose_name='В какую секунду вызвать')),
                ('kwargs', models.JSONField(verbose_name='Переменные, которые передаются в функцию')),
            ],
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
