# Generated by Django 2.0 on 2018-10-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20181019_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectconnected',
            name='ip',
            field=models.CharField(default='default_ip', max_length=100),
        ),
    ]
