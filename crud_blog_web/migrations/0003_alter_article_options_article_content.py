# Generated by Django 5.1.6 on 2025-02-23 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_blog_web', '0002_article_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Artykuły'},
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='Default content'),
            preserve_default=False,
        ),
    ]
