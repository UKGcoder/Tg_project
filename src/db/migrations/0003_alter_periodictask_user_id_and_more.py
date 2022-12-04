# Generated by Django 4.1.3 on 2022-12-03 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_periodictask_rename_users_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodictask',
            name='user_id',
            field=models.BigIntegerField(verbose_name='ID пользователя в Телеграмм'),
        ),
        migrations.AlterField(
            model_name='roundvideo',
            name='chat_tg_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='roundvideo',
            name='user_tg_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='support',
            name='chat_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='support',
            name='user_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='supt',
            name='chat_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='supt',
            name='user_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.BigIntegerField(verbose_name='ID пользователя в Телеграмм'),
        ),
    ]
