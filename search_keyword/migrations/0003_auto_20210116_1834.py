# Generated by Django 3.1.2 on 2021-01-16 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_keyword', '0002_auto_20210115_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='score',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]