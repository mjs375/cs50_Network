# Generated by Django 3.1.3 on 2020-11-15 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_auto_20201111_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likers',
        ),
    ]
