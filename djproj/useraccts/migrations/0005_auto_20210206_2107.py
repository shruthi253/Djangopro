# Generated by Django 3.1.5 on 2021-02-06 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccts', '0004_auto_20210206_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.CharField(max_length=50),
        ),
    ]