# Generated by Django 4.1.7 on 2023-03-20 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productAndReviews', '0004_rename_review_review_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(max_length=200),
        ),
    ]