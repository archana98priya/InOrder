# Generated by Django 2.1.3 on 2018-11-03 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.IntegerField(default=2, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='bill_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='orders.Bill'),
        ),
    ]
