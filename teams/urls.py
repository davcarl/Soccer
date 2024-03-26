from django.urls import path

from .models import Coach
from .views import (Home, Teams,
                CreateTeamView, TeamDetailView,
                TeamUpdateView, DeleteTeamView, 
                
                AddPlayerView,PlayerDetailView,
                UpdatePlayerView,DeletePlayerView,

                CoachView, CreateCoachView,CoachDetailView,
                UpdateCoachView,DeleteCoachView,

                RefView,CreateRefView,
                RefDetailView, DeleteRefView,
                UpdateRefView,
            )



urlpatterns = [
    path("",Home.as_view(), name="home"),
    path('teams/', Teams.as_view(), name='teams'),
    path('createteam/', CreateTeamView.as_view(), name='create_team'),
    path('teams/<int:pk>/',TeamDetailView.as_view(),name='team_details'),
    path('teams/update/<int:pk>/', TeamUpdateView.as_view(), name='team_update'),
    path('teams/deleteteam/<int:pk>/', DeleteTeamView.as_view(), name='delete_team'),

    path('teams/addplayer/', AddPlayerView.as_view(), name='add_player'),
    path('teams/deleteplayer/<int:pk>/', DeletePlayerView.as_view(), name='delete_player'),
    path('teams/editplayer/<int:pk>/',UpdatePlayerView.as_view(),name='edit_player'),
    path('teams/teams/<int:pk>/',PlayerDetailView.as_view(),name='player_details'),

    path('coach/', CoachView.as_view(), name='coach'),
    path('coach/createcoach/', CreateCoachView.as_view(), name='create_coach'),
    path('coach/deletecoach/<int:pk>/', DeleteCoachView.as_view(), name='delete_coach'),
    path('coach/updatecoach/<int:pk>/',UpdateCoachView.as_view(),name='update_coach'),
    path('coach/<int:pk>/',CoachDetailView.as_view(),name='coach_details'),

    path('ref/', RefView.as_view(), name='ref'),
    path('ref/createref/', CreateRefView.as_view(), name='create_ref'),
    path('ref/deleteref/<int:pk>/', DeleteRefView.as_view(), name='delete_ref'),
    path('ref/updateref/<int:pk>/',UpdateRefView.as_view(),name='update_ref'),
    path('ref/<int:pk>/',RefDetailView.as_view(),name='ref_details'),   
        ]
        