# Generated by Django 5.0.2 on 2024-02-23 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_rename_userdata_authordatamodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdatamodel',
            name='book_price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]