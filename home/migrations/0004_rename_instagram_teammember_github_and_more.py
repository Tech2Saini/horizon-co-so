# Generated by Django 5.1.6 on 2025-03-15 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_github_teammember_instagram_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teammember',
            old_name='instagram',
            new_name='github',
        ),
        migrations.RenameField(
            model_name='teammember',
            old_name='twitter',
            new_name='portfolio',
        ),
    ]
