# Generated by Django 5.0.2 on 2024-03-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_secu', '0016_remove_uploadhistory_hash_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='hash_value',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]