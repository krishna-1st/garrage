# Generated by Django 5.0 on 2023-12-13 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]
