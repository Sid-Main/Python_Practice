# Generated by Django 5.2 on 2025-04-09 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_objects_offers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Offers',
            new_name='Offer',
        ),
    ]
