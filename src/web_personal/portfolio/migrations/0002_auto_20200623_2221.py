# Generated by Django 3.0.7 on 2020-06-24 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'ordering': ['-created'], 'verbose_name': 'projecto', 'verbose_name_plural': 'projectos'},
        ),
    ]
