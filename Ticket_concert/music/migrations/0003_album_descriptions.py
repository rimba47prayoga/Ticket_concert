# Generated by Django 2.0.4 on 2018-04-21 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_album_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='descriptions',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
