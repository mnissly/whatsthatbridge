# Generated by Django 3.0.5 on 2020-05-08 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bridge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bridge',
            name='picture',
            field=models.CharField(default='../../static/bridge/default_bridge.jpg', max_length=600),
        ),
    ]
