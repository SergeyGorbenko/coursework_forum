# Generated by Django 2.1.4 on 2018-12-23 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20181223_0327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='count_comments',
        ),
    ]