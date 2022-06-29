# Generated by Django 4.0.4 on 2022-06-27 22:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kleverApp', '0020_article_added_date_article_font_alter_article_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='added_date',
            new_name='published_at',
        ),
        migrations.AddField(
            model_name='article',
            name='isFeatured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='thumbnail_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='videos',
            name='isFeatured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='videos',
            name='published_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='videos',
            name='thumbnail_url',
            field=models.CharField(max_length=255),
        ),
    ]