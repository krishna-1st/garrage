# Generated by Django 5.0 on 2023-12-14 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0007_alter_form_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='username',
        ),
    ]
