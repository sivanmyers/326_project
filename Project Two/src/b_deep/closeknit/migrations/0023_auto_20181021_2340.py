# Generated by Django 2.1.1 on 2018-10-21 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closeknit', '0022_auto_20181021_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_stamp',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_stamp',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='reaction',
            name='time_stamp',
            field=models.DateTimeField(blank=True),
        ),
    ]
