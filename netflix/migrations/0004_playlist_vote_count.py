# Generated by Django 3.2.5 on 2021-07-22 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0003_playlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='vote_count',
            field=models.IntegerField(default=0),
        ),
    ]
