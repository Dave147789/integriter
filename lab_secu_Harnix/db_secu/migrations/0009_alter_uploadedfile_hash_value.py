# Generated by Django 5.0.2 on 2024-03-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_secu', '0008_alter_uploadedfile_hash_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='hash_value',
            field=models.CharField(max_length=64),
        ),
    ]
