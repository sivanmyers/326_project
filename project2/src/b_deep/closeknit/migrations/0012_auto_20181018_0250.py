# Generated by Django 2.1.1 on 2018-10-18 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closeknit', '0011_auto_20181018_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_stamp',
            field=models.DateTimeField(default='2018-10-17 10:49'),
        ),
    ]
