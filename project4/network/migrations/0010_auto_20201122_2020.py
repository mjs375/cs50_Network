# Generated by Django 3.1.3 on 2020-11-22 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_auto_20201120_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='postuser',
        ),
    ]
