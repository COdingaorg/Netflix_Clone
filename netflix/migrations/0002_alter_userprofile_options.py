# Generated by Django 3.2.5 on 2021-07-22 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['-id']},
        ),
    ]
