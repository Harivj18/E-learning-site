# Generated by Django 3.2.3 on 2021-07-07 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210707_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='Content',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
