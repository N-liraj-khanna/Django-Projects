# Generated by Django 3.2.5 on 2021-07-24 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=10000)),
                ('uuid', models.CharField(max_length=15)),
            ],
        ),
    ]
