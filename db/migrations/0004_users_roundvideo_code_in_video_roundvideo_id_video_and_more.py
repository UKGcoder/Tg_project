# Generated by Django 4.1.2 on 2022-11-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_roundvideo_chat_tg_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=20)),
                ('action', models.CharField(max_length=20)),
                ('additional_action', models.CharField(max_length=20)),
                ('start_disput', models.CharField(max_length=10)),
                ('deposit', models.IntegerField()),
                ('promocode_user', models.CharField(max_length=10)),
                ('promocode_from_friend', models.CharField(max_length=10)),
                ('count_days', models.IntegerField()),
                ('number_dispute', models.CharField(max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name='roundvideo',
            name='code_in_video',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='roundvideo',
            name='id_video',
            field=models.IntegerField(default=1111),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='roundvideo',
            name='status',
            field=models.CharField(choices=[('good', 'Good'), ('bad', 'Bad'), ('other', 'Other')], max_length=20, verbose_name='Статус кружочка'),
        ),
    ]