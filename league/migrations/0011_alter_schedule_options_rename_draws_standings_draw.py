# Generated by Django 4.1 on 2022-08-25 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0010_schedule_assistant_ref_schedule_away_team_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedule',
            options={'verbose_name': 'Schedule', 'verbose_name_plural': 'Schedules'},
        ),
        migrations.RenameField(
            model_name='standings',
            old_name='draws',
            new_name='draw',
        ),
    ]
