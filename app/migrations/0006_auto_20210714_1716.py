# Generated by Django 3.2.3 on 2021-07-14 11:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Content',
        ),
        migrations.AddField(
            model_name='comment',
            name='Thumbnail',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='dp/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
