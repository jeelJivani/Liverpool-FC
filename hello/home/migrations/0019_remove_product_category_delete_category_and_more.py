# Generated by Django 4.2.4 on 2023-10-02 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
