from django.db import models
from django.utils.translation import gettext_lazy as _
from smart_selects.db_fields import ChainedManyToManyField, ChainedForeignKey, GroupedForeignKey
from django.utils.timezone import now
from teams.fields import CaseInsensitiveCharField
from branch.models import Branch
from teams.models import Ref, Team, Player
from django.contrib.auth.models import User
from itertools import combinations

STANDINGS_ORDER_HUMAN = (
    (0, _('Matches, Points, Wins, Lost, Draw, Goals_For, Goals_Aganist,Goal_Diff')), 
    (1, _('Matches, Wins, Lost, Draw, Goals_For, Goals_Aganist,Goal_Diff, Points')), 
)
STANDINGS_ORDER = (
    (0, ('-points', 'goal_diff', 'goals_for')), 
    (1, ('-points', 'win', 'lost','draw')), 
)

class League(models.Model):
    name=CaseInsensitiveCharField(max_length=100)
    branch= models.ForeignKey(Branch,on_delete=models.CASCADE, related_name='branch')
    admin = models.OneToOneField(User, on_delete= models.SET_NULL, null= True)


    def __str__(self) -> str:
        return f'FKF {self.branch} {self.name} league'

class Season(models.Model):
    league = models.OneToOneField(League, null=True, on_delete=models.CASCADE, related_name=_('League'))
    slug = models.SlugField(unique=True, null=True, verbose_name=_('Slug'))
    teams = models.ManyToManyField(Team, blank=True, related_name='teams', verbose_name=_('Teams'))
    standings_order = models.IntegerField(verbose_name=_('Standings order'),
        choices=(STANDINGS_ORDER_HUMAN),
        default=0
    )
    win_points = models.IntegerField(null=True, blank=False, default=0, verbose_name=_('Points for win'))
    lost_points = models.IntegerField(null=True, blank=False, default=0, verbose_name=_('Points for loss'))
    draw_points = models.IntegerField(null=True, blank=False, default=0, verbose_name=_('Points for draw'))
    
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    registration_deadline= models.DateTimeField(null=True)
    transfer_deadline=models.DateTimeField(null=True)
    max_players=models.PositiveIntegerField(default=25)
    
    class Meta:
        verbose_name = _('Season')
        verbose_name_plural = _('Seasons')

    @property
    def season_name(self):
        return f'{self.league}: {self.start_date.year}/{self.end_date.year}'
    
    def __str__(self):
        return self.season_name     
        
class Match (models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE,null=True, related_name='home_team', verbose_name=_('Home team'))
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE,null=True, related_name='away_team', verbose_name=_('Away team'))
    home_team_score = models.IntegerField(null=True, blank=True, verbose_name=_('Home team score'))
    away_team_score = models.IntegerField(null=True, blank=True, verbose_name=_('Away team score'))
    date = models.DateTimeField(default=now, verbose_name=_('Date'))
    venue = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('Venue'))
    cente_ref = models.ForeignKey(Ref, related_name='CR',
        on_delete=models.SET_NULL, null=True, limit_choices_to={'position':'CR'})
    assistant_ref = models.ForeignKey(Ref, related_name='AR',
        on_delete=models.SET_NULL, null=True, limit_choices_to={'position':'AR'})

    def __str__(self) -> str:
        return f'{self.home_team} VS {self.away_team} on {self.date}'

    class Meta():
        abstract = True

class Schedule(Match):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, verbose_name=_('Season'))
    week = models.IntegerField(null=False, blank=False, default=1, verbose_name=_('Week'))

    class Meta:
        verbose_name = _('Schedule')
        verbose_name_plural = _('Schedules')

    def __str__(self):
        return f'{self.season} {self.week}'



class Standings(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, verbose_name=_('Season'))
    team = ChainedForeignKey(Team, chained_field='season', chained_model_field='teams', related_name='team', verbose_name=_('Team'))
    position = models.IntegerField(null=True, blank=True, default=1, verbose_name=_('Position'))
    matches = models.IntegerField(null=True, blank=True, default=0, verbose_name=_('Matches'))
    win = models.IntegerField(null=True, blank=False, default=0, verbose_name=_('Won'))
    lost = models.IntegerField(null=True, blank=False, default=0, verbose_name=_('Lost'))
    draw = models.IntegerField(null=True, blank=False, default=0, verbose_name=_('Draw'))
    goals_for = models.IntegerField(null=True, blank=False, default=0, verbose_name=_('GF'))
    goals_aganist = models.IntegerField(null=True, blank=False, default=0, verbose_name=_('GA'))
    points = models.IntegerField(null=True, blank=False, default=0, verbose_name=_('Points'))
    goal_diff =models.IntegerField(null=True, blank=False, default=0, verbose_name=_('GD'))
    
    @property
    def goal_dif(self):
        self.goal_diff = self.goals_for - self.goals_aganist
        return self.goal_diff


    def __str__(self):
        return "{0} {1}".format(self.season, self.team)

    class Meta:
        ordering = STANDINGS_ORDER[0][1]
        unique_together = ('season', 'team')
        verbose_name = _('Table')
        verbose_name_plural = _('Tables')
    
# Create your models here.
