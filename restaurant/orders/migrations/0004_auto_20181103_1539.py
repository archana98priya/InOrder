# Generated by Django 2.1.3 on 2018-11-03 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20181103_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='orders.Item'),
        ),
    ]
