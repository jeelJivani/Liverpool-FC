# Generated by Django 4.2.4 on 2023-09-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_blog_blog_view_count_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_view_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
