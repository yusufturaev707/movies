# Generated by Django 3.2.9 on 2021-11-03 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20211103_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='description_uz',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='name_uz',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description_uz',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_uz',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='descriptions_uz',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='name_uz',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='country_uz',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='descriptions_uz',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='tagline_uz',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='title_uz',
        ),
        migrations.RemoveField(
            model_name='movieshots',
            name='descriptions_uz',
        ),
        migrations.RemoveField(
            model_name='movieshots',
            name='title_uz',
        ),
    ]