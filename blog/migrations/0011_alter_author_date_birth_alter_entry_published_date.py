# Generated by Django 4.1.3 on 2022-12-29 16:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_entry_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_birth',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='published_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
