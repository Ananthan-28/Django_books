# Generated by Django 5.0.2 on 2024-02-25 16:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_rename_product_name_addtocartmodel_product_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewModal',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('review_content', models.TextField(max_length=255)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.bookdatamodel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.authordatamodel')),
            ],
            options={
                'db_table': 'review_data',
            },
        ),
    ]
