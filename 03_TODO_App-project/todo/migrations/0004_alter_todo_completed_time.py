# Generated by Django 3.2.4 on 2021-06-22 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]