# Generated by Django 3.1.6 on 2021-08-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210820_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_thumb',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
