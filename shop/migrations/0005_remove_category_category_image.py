# Generated by Django 4.2.1 on 2023-05-13 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_customer_date_of_birth_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_image',
        ),
    ]