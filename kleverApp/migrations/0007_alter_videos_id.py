# Generated by Django 4.0.4 on 2022-06-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kleverApp', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]