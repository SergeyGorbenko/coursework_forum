# Generated by Django 2.1.4 on 2018-12-21 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20181220_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='theme',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
