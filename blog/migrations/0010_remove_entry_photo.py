# Generated by Django 4.1.3 on 2022-12-29 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_entry_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='photo',
        ),
    ]
