# Generated by Django 4.1.7 on 2023-03-19 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productAndReviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='cateory',
            new_name='category',
        ),
    ]
