# Generated by Django 4.1.13 on 2024-04-11 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='property-list/images/')),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=512)),
                ('price', models.IntegerField()),
                ('number_of_bedrooms', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
    ]