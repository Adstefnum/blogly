# Generated by Django 3.0 on 2020-07-19 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200717_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comments_post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Blog'),
        ),
    ]
