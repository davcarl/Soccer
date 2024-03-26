from django.contrib import admin
from django.db import models
from django.db.models import Q
from django.db.models.signals import m2m_changed
from django.forms import TextInput, Textarea, IntegerField
from .models import League, Season, Schedule, Standings, STANDINGS_ORDER
from django.utils import timezone
from teams.models import Team, Player
from itertools import combinations




def standings_save(instance):
        season = Season.objects.get(pk=instance.pk)

        for team in season.teams.all():
            obj, created = Standings.objects.get_or_create(season = season, team = team)
        
        standings = Standings.objects.filter(season = season).exclude(team__in = season.teams.all())
        for team in standings:
                team.delete()

def standings_position_update(season):
    order = STANDINGS_ORDER[season.standings_order][1]
    standings = Standings.objects.filter(season = season.pk).order_by(*order)
    position = 0
    for team in standings:
        position += 1
        team.position = position
        team.save()

def standings_update(instance):
        standings = Standings.objects.filter(season = instance.pk)
        now = timezone.now()
        for standing in standings:
            points = 0
            wins = 0
            lost = 0
            draws = 0
            matches = 0
            goals_for = 0
            goals_aganist = 0
            team = standing.team
            team_schedule = Schedule.objects.filter(Q(home_team=team) | Q(away_team=team), season = instance.pk, date__lte=now )
            for match in team_schedule:
                matches += 1
                if not match.home_team_score:
                    match.home_team_score = 0
                if not match.away_team_score:
                    match.away_team_score = 0

                if match.home_team == team:
                    goals_for += match.home_team_score
                    goals_aganist += match.away_team_score
                    if match.home_team_score > match.away_team_score:
                        wins += 1
                        points += instance.win_points
                    elif match.home_team_score < match.away_team_score:
                        lost += 1
                        points += instance.lost_points
                    else:
                        draws += 1
                        points += instance.draw_points

                if match.away_team == team:
                    goals_for += match.away_team_score
                    goals_aganist += match.home_team_score
                    if match.away_team_score > match.home_team_score:
                        wins += 1
                        points += instance.win_points
                    elif match.away_team_score < match.home_team_score:
                        lost += 1
                        points += instance.lost_points
                    else:
                        draws += 1
                        points += instance.draw_points

                standing.points = points
                standing.win = wins
                standing.lost = lost
                standing.draws = draws
                standing.goals_for = goals_for
                standing.goals_aganist = goals_aganist
                standing.matches = matches
                standing.save()
        standings_position_update(instance)




class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'short_name')
    prepopulated_fields = {'slug': ('short_name',), }

class ScheduleInline(admin.TabularInline):
    model = Schedule
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'style':'width: 20px;'})},
    }

class StandingsInline(admin.TabularInline):
    model = Standings
    ordering = ('position', '-points')
    exclude = ('matches', 'win', 'lost', 'draw', 'GF', 'GA')
    max_num=0
    actions = []
    readonly_fields = ('team',)
    fields = ('team', 'points', 'position')




class SeasonAdmin(admin.ModelAdmin):
    inlines = [
        StandingsInline, 
        ScheduleInline,
    ]
    prepopulated_fields = {'slug': ('start_date', 'league',), }

    def create_schedule(instance):
        season = Season.objects.get(pk=instance.pk)
        for team in season.teams.all():
            teams_combinations = combinations(Team.objects.filter(season=season.pk), 2)
            list_teams_combinations = list(teams_combinations)
            for combination in list_teams_combinations:
                match = Schedule.objects.create(week=week)
                match.teams.add(combination[0])
                match.teams.add(combination[1])
                match.save()
        create_schedule(instance)
        

    def save_model(self, request, obj, form, change):
        obj.save()
        form.save_m2m()
        standings_save(obj)
        standings_update(obj)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','position','team')
    list_filter = ('team','position')
        
admin.site.register(League)
admin.site.register(Team, TeamAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Player, PlayerAdmin)
    
# Register your models here.
