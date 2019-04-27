# Generated by Django 2.2 on 2019-04-27 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='bill',
            name='discount_end',
            field=models.DateField(blank=True),
        ),
    ]