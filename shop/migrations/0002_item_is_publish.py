# Generated by Django 2.2 on 2019-05-01 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_publish',
            field=models.BooleanField(default=False),
        ),
    ]