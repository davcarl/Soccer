# Generated by Django 4.1 on 2022-08-25 11:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0014_team_short_name_team_slug'),
        ('league', '0009_alter_standings_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='assistant_ref',
            field=models.ForeignKey(limit_choices_to={'position': 'AR'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AR', to='teams.ref'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='away_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='teams.team', verbose_name='Away team'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='away_team_score',
            field=models.IntegerField(blank=True, null=True, verbose_name='Away team score'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='cente_ref',
            field=models.ForeignKey(limit_choices_to={'position': 'CR'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CR', to='teams.ref'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='home_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='teams.team', verbose_name='Home team'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='home_team_score',
            field=models.IntegerField(blank=True, null=True, verbose_name='Home team score'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='venue',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Venue'),
        ),
        migrations.DeleteModel(
            name='Match',
        ),
    ]
