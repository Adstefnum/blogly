# Generated by Django 2.2.16 on 2020-12-16 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200723_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
