# Generated by Django 3.2.3 on 2021-08-03 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_page_dp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='Content',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
