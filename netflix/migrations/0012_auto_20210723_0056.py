# Generated by Django 3.2.5 on 2021-07-22 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0011_alter_playlist_popularity'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='poster_path',
            field=models.CharField(default='Nadia', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playlist',
            name='release_date',
            field=models.CharField(default='Nadia', max_length=200),
            preserve_default=False,
        ),
    ]
