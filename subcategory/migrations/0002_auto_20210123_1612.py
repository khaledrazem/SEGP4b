# Generated by Django 3.1.3 on 2021-01-23 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcategory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='trend_score',
            field=models.IntegerField(),
        ),
    ]
