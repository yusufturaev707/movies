# Generated by Django 3.2.8 on 2021-10-28 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20211028_1200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'verbose_name': 'Aktyor va Rejissiyor', 'verbose_name_plural': 'Aktyorlar va Rejissiyorlar'},
        ),
    ]