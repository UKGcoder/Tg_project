# Generated by Django 4.1.2 on 2022-11-13 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_roundvideo_type_video_alter_roundvideo_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('id_dispute', models.IntegerField()),
                ('chat_id', models.IntegerField()),
                ('problem', models.CharField(max_length=256)),
                ('solved', models.CharField(choices=[('new', 'New'), ('done', 'Done'), ('in_process', 'In Process')], max_length=10, verbose_name='статус вопроса')),
            ],
        ),
        migrations.AlterField(
            model_name='roundvideo',
            name='status',
            field=models.CharField(choices=[('good', 'Good'), ('bad', 'Bad'), ('other', 'Other')], max_length=20, verbose_name='Статус кружочка'),
        ),
    ]
