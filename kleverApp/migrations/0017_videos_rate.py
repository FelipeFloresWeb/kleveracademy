# Generated by Django 4.0.4 on 2022-06-19 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kleverApp', '0016_remove_ratevideo_rate_calc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='rate',
            field=models.FloatField(default=0),
        ),
    ]
