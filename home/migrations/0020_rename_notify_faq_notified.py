# Generated by Django 5.1.6 on 2025-03-18 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_faq_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faq',
            old_name='notify',
            new_name='notified',
        ),
    ]
