# Generated by Django 2.0.5 on 2018-11-03 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20181103_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(default=None, upload_to='restaurant'),
        ),
    ]
