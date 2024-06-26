# Generated by Django 4.1.7 on 2023-04-26 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0013_blogerpromocodes'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisputeAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, verbose_name='Имя пользователя в TG')),
                ('user_id', models.BigIntegerField(verbose_name='id пользователя в рамках админ бота')),
                ('chat_id', models.BigIntegerField(blank=True, null=True, verbose_name='id пользователя в рамках админ бота')),
                ('is_super_admin', models.BooleanField(default=False, verbose_name='Является ли админ супер-админом?')),
            ],
        ),
    ]
