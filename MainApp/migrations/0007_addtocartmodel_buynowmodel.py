# Generated by Django 5.0.2 on 2024-02-25 07:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_authordatamodel_author_login_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddToCartModel',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('cart_quantity', models.IntegerField()),
                ('product_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.bookdatamodel')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.authordatamodel')),
            ],
            options={
                'db_table': 'cart_data',
            },
        ),
        migrations.CreateModel(
            name='BuyNowModel',
            fields=[
                ('buy_id', models.AutoField(primary_key=True, serialize=False)),
                ('buy_quantity', models.IntegerField()),
                ('product_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.bookdatamodel')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.authordatamodel')),
            ],
            options={
                'db_table': 'buy_data',
            },
        ),
    ]
