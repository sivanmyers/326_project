# Generated by Django 2.1.1 on 2018-10-28 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('closeknit', '0023_auto_20181021_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img_content',
        ),
    ]
