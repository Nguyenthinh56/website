# Generated by Django 5.1.3 on 2024-11-07 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='produce',
            new_name='product',
        ),
    ]
