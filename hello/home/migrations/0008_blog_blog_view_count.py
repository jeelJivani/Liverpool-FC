# Generated by Django 4.2.4 on 2023-09-01 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_blog_blog_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_view_count',
            field=models.IntegerField(default=1),
        ),
    ]