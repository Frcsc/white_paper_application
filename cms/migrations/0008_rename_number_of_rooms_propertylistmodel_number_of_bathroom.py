# Generated by Django 4.1.13 on 2024-04-14 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_remove_propertylistmodel_number_of_bathrooms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertylistmodel',
            old_name='number_of_rooms',
            new_name='number_of_bathroom',
        ),
    ]
