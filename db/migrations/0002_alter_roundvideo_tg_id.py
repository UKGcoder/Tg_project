# Generated by Django 4.1.2 on 2022-11-01 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roundvideo',
            name='tg_id',
            field=models.CharField(max_length=90),
        ),
    ]
