# Generated by Django 5.0 on 2023-12-13 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='current_role',
            field=models.CharField(choices=[('role_option_1', 'DBA'), ('role_option_2', 'SE1'), ('role_option_3', 'SE2')], default='default_role_value', max_length=80),
        ),
        migrations.AddField(
            model_name='form',
            name='recommend',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='default_role_value', max_length=50),
        ),
        migrations.AddField(
            model_name='form',
            name='useful',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='default_role_value', max_length=50),
        ),
    ]
