# Generated by Django 5.0.4 on 2024-05-30 01:27

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_alter_checkout_estimated_arrival'),
        ('retail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='estimated_arrival',
            field=models.DateField(default=datetime.datetime(2024, 6, 13, 1, 27, 20, 898750, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='AnonymousOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('purchase_day', models.DateTimeField(default=django.utils.timezone.now)),
                ('estimated_arrival', models.DateField(default=datetime.datetime(2024, 6, 13, 1, 27, 20, 899748, tzinfo=datetime.timezone.utc))),
                ('address', models.CharField(max_length=1000)),
                ('paying_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.payingmethod')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.status')),
            ],
        ),
        migrations.CreateModel(
            name='AnonymousOrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('anonymousorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.anonymousorder')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.product')),
            ],
        ),
    ]
