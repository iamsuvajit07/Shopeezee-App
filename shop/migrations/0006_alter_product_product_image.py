# Generated by Django 4.2.1 on 2023-05-22 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_category_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='productImg/'),
        ),
    ]