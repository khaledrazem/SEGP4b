# Generated by Django 3.1.2 on 2021-01-28 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search_keyword', '0001_initial'),
        ('subcategory', '0001_initial'),
        ('paper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper_keyword_relationship',
            name='paper_keyword_1',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='paper_keyword_1', to='search_keyword.keyword'),
        ),
        migrations.AlterField(
            model_name='paper_keyword_relationship',
            name='paper_keyword_2',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paper_keyword_2', to='search_keyword.keyword'),
        ),
        migrations.AlterField(
            model_name='paper_subcategory_relationship',
            name='paper_subcategory_1',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='paper_subcategory_1', to='subcategory.subcategory'),
        ),
        migrations.AlterField(
            model_name='paper_subcategory_relationship',
            name='paper_subcategory_2',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paper_subcategory_2', to='subcategory.subcategory'),
        ),
    ]
