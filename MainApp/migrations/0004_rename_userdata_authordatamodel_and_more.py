# Generated by Django 5.0.2 on 2024-02-21 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_alter_bookdata_book_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserData',
            new_name='AuthorDataModel',
        ),
        migrations.RenameModel(
            old_name='BookCategory',
            new_name='BookCategoryModel',
        ),
        migrations.RenameModel(
            old_name='BookData',
            new_name='BookDataModel',
        ),
    ]