# Generated by Django 3.1.2 on 2021-01-29 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcategory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='quick_search_data',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
