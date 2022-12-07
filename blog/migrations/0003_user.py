# Generated by Django 4.1.3 on 2022-12-07 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_entry_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=100, verbose_name='Apellido')),
                ('document', models.IntegerField(verbose_name='DNI')),
                ('salary', models.IntegerField(verbose_name='Sueldo')),
                ('date_birth', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
            ],
        ),
    ]
