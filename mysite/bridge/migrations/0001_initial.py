# Generated by Django 3.0.5 on 2020-05-04 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=600)),
                ('description', models.CharField(default='this bridge has no description', max_length=600)),
                ('year_built', models.CharField(default='this bridge has no information on year built', max_length=600)),
            ],
        ),
    ]
