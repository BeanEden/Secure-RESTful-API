# Generated by Django 4.0.4 on 2022-07-28 08:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softdesk', '0007_alter_contributor_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(default='undefined', max_length=255, unique=True, validators=[django.core.validators.RegexValidator(message='characters must be Alphanumeric', regex='[a-zA-Z0-9\\s]')]),
        ),
    ]
