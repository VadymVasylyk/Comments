# Generated by Django 5.0.1 on 2024-01-12 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_messages_alter_profile_img'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Messages',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
