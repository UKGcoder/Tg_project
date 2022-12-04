# Generated by Django 4.1.2 on 2022-10-29 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoundVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.IntegerField()),
                ('user_tg_id', models.IntegerField()),
                ('status', models.CharField(choices=[('good', 'Good'), ('bad', 'Bad')], max_length=20,
                                            verbose_name='Статус кружочка')),
            ],
        ),
    ]
