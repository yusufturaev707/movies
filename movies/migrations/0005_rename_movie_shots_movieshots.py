# Generated by Django 3.2.8 on 2021-10-31 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_actor_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movie_shots',
            new_name='MovieShots',
        ),
    ]
