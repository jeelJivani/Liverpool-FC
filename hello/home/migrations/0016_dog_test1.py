# Generated by Django 4.2.4 on 2023-09-29 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_delete_dog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('data', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hcc_24_code', models.IntegerField(blank=True, null=True)),
                ('hcc_28_code', models.IntegerField(blank=True, null=True)),
                ('place_of_service', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
