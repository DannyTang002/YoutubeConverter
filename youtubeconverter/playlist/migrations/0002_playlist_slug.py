# Generated by Django 4.1.5 on 2023-02-16 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]