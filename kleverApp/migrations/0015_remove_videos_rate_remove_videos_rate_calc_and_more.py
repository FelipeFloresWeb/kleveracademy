# Generated by Django 4.0.4 on 2022-06-19 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kleverApp', '0014_alter_favoritevideo_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videos',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='videos',
            name='rate_calc',
        ),
        migrations.RemoveField(
            model_name='videos',
            name='rate_length',
        ),
        migrations.CreateModel(
            name='RateVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(default=0)),
                ('rate_length', models.IntegerField(default=0)),
                ('rate_calc', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate_videos', to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate_videos', to='kleverApp.videos')),
            ],
        ),
    ]