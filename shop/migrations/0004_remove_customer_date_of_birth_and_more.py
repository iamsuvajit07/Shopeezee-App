# Generated by Django 4.2.1 on 2023-05-13 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_customer_gender_alter_customer_mobile_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='date_of_birth',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=200),
        ),
    ]