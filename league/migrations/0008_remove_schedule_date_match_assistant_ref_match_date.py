# Generated by Django 4.1 on 2022-08-25 10:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0014_team_short_name_team_slug'),
        ('league', '0007_remove_schedule_away_team_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='date',
        ),
        migrations.AddField(
            model_name='match',
            name='assistant_ref',
            field=models.ForeignKey(limit_choices_to={'position': 'AR'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AR', to='teams.ref'),
        ),
        migrations.AddField(
            model_name='match',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
    ]
