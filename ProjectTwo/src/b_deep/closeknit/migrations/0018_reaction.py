# Generated by Django 2.1.1 on 2018-10-18 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closeknit', '0017_auto_20181018_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('0', 'None'), ('1', 'React 1'), ('2', 'React 2'), ('3', 'React 3'), ('4', 'React 4'), ('5', 'React 5')], default='0', max_length=1)),
            ],
        ),
    ]
