# Generated by Django 4.1 on 2022-08-23 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name': 'branch', 'verbose_name_plural': 'branches'},
        ),
        migrations.AlterModelOptions(
            name='subbranch',
            options={'verbose_name': 'sub branch', 'verbose_name_plural': 'sub branches'},
        ),
    ]
