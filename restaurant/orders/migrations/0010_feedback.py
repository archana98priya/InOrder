# Generated by Django 2.0.5 on 2018-11-03 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_restaurant_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_back', models.TextField(max_length=255)),
                ('cust_id', models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='orders.Customer')),
                ('rest_id', models.ForeignKey(default=1007, on_delete=django.db.models.deletion.CASCADE, to='orders.Restaurant')),
            ],
        ),
    ]
