
from django.urls import re_path, path

from .views import ( LeagueDetail, Leagues, StandingsFull, 
    TeamDetails, ScheduleFull, TeamSchedule, TeamRoster)

urlpatterns = [
    path('leagues/', Leagues.as_view(), name='leagues'),
    path('leagues/<int:pk>/', LeagueDetail.as_view(), name='league_details'),


    re_path(r'^(?P<season>[-\w]+)/standings$', StandingsFull.as_view(), name='standings_full' ),
    re_path(r'^(?P<season>[-\w]+)/schedule$', ScheduleFull.as_view(), name='schedule_full' ),
    re_path(r'^(?P<season>[-\w]+)/team/(?P<team>[-\w]+)$', TeamDetails.as_view(), name='team_detail' ),
    re_path(r'^(?P<season>[-\w]+)/team/(?P<team>[-\w]+)/roster$', TeamRoster.as_view(), name='team_roster' ),
    re_path(r'^(?P<season>[-\w]+)/team/(?P<team>[-\w]+)/schedule$', TeamSchedule.as_view(), name='team_schedule' ),
]