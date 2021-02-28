# Generated by Django 3.1.3 on 2021-02-09 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combinations', '0003_subcategory_combination_quick_search_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory_combination',
            name='combination_authorscore',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='subcategory_combination',
            name='combination_growth',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='subcategory_combination',
            name='combination_score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]