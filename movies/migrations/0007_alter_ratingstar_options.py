# Generated by Django 3.2.8 on 2021-11-03 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20211031_1810'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Yulduz reytingi', 'verbose_name_plural': 'Yulduzlar reytingi'},
        ),
    ]
