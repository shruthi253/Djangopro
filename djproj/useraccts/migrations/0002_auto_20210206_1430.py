# Generated by Django 3.1.5 on 2021-02-06 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='item',
            new_name='item_name',
        ),
    ]
