
from django import forms
from .models import Coach, Ref, SubCounty, Team, Player
from datetime import datetime

class RefForm (forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={
            'type': 'date'}))
    class Meta():
        model = Ref
        fields=[
            'id_No','birth_date','county',
            'sub_county','position',
            ]

class CoachForm (forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={
            'type': 'date'}))
    class Meta():
        model = Coach
        fields=[
            'id_No','birth_date','county',
            'sub_county',
            ]
    

class TeamForm (forms.ModelForm):
    class Meta():
        model = Team
        fields = ['logo', 'team_name',
        'coach','location_name',
        'county','sub_county'
            ]
        
 
class PlayerForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={
            'type': 'date'}))
    class Meta():
        model = Player
        fields = [ 'avatar','first_name','last_name', 'id_birth_cert_no',
        'birth_date', 'county', 'sub_county' ,'position',
            ]
