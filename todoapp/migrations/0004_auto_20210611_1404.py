# Generated by Django 3.2 on 2021-06-11 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_rename_pubished_todomodel_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='published',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]