# Generated by Django 3.1.5 on 2021-02-06 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20210129_2006'),
        ('useraccts', '0003_items_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.destination'),
        ),
    ]
