# Generated by Django 4.1.5 on 2023-02-01 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0002_video_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
