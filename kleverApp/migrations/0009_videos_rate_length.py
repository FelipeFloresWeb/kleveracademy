# Generated by Django 4.0.4 on 2022-06-19 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kleverApp', '0008_favoritevideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='rate_length',
            field=models.IntegerField(default=0),
        ),
    ]