# Generated by Django 4.1.13 on 2024-04-11 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_peoplemodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='peoplemodel',
            options={'verbose_name_plural': 'People'},
        ),
        migrations.AddField(
            model_name='peoplemodel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
