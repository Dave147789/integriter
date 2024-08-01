# Generated by Django 5.0.2 on 2024-03-03 19:15

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_secu', '0021_uploadhistory_client'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='client',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('groups__name__in', ['Interne']), _negated=True), models.Q(('is_staff', True), _negated=True)), on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(upload_to='uploaded_files/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['txt'])]),
        ),
    ]