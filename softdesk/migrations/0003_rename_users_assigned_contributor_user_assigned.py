# Generated by Django 4.0.4 on 2022-06-30 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('softdesk', '0002_project_contributor_user_projects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contributor',
            old_name='users_assigned',
            new_name='user_assigned',
        ),
    ]
