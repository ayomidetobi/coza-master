# Generated by Django 3.2.16 on 2022-11-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloth', '0005_auto_20221124_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
