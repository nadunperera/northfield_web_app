# Generated by Django 2.2 on 2019-04-29 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20190429_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='provider',
        ),
    ]