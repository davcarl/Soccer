# Generated by Django 4.1 on 2022-08-24 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0005_league_admin_alter_league_branch_alter_season_league'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='name',
        ),
    ]
