# Generated by Django 4.1.7 on 2023-04-03 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_one_bread_created_at_one_bread_order_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='one_bread_order',
            old_name='number',
            new_name='bread_number',
        ),
    ]
