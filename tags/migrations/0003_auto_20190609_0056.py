# Generated by Django 2.2.1 on 2019-06-08 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_auto_20190530_0132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
