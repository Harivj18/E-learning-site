# Generated by Django 3.2.3 on 2021-07-14 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210714_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Thumbnail',
        ),
    ]