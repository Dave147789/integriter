# Generated by Django 5.0.2 on 2024-03-03 13:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_secu', '0003_uploadedfile_hash_value_uploadhistory_hash_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadhistory',
            name='download_time',
        ),
        migrations.RemoveField(
            model_name='uploadhistory',
            name='hash_value',
        ),
        migrations.AddField(
            model_name='uploadhistory',
            name='upload_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
