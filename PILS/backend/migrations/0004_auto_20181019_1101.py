# Generated by Django 2.0 on 2018-10-19 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_action_constructeur'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bouton',
            old_name='action',
            new_name='id_action',
        ),
        migrations.RemoveField(
            model_name='action',
            name='commentaire',
        ),
        migrations.RemoveField(
            model_name='action',
            name='constructeur',
        ),
        migrations.AddField(
            model_name='action',
            name='action',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='action',
            name='id_object',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bouton',
            name='name',
            field=models.CharField(default='default_name', max_length=100),
        ),
    ]
