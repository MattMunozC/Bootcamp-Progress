# Generated by Django 5.0.4 on 2024-06-01 17:20

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_address_resume'),
        ('checkout', '0004_anonymousorder_seller_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.address'),
        ),
        migrations.AlterField(
            model_name='anonymousorder',
            name='estimated_arrival',
            field=models.DateField(default=datetime.datetime(2024, 6, 15, 17, 20, 3, 996715, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='estimated_arrival',
            field=models.DateField(default=datetime.datetime(2024, 6, 15, 17, 20, 3, 995718, tzinfo=datetime.timezone.utc)),
        ),
    ]
