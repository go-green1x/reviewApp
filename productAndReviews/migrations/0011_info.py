# Generated by Django 4.1.7 on 2023-03-21 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productAndReviews', '0010_alter_review_date_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.EmailField(max_length=254)),
                ('status', models.BooleanField()),
            ],
        ),
    ]
