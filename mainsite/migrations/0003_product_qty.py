# Generated by Django 2.0.4 on 2018-04-14 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20180414_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.PositiveIntegerField(default=0, verbose_name='库存'),
        ),
    ]
