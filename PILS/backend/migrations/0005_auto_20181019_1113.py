# Generated by Django 2.0 on 2018-10-19 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20181019_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='action',
        ),
        migrations.AddField(
            model_name='action',
            name='descriptif',
            field=models.CharField(default='default_description', max_length=100),
        ),
    ]
