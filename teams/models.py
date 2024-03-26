from email.policy import default
from itertools import count
from django.db import models
from PIL import Image
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse
from .fields import CaseInsensitiveCharField
from datetime import datetime, date
from smart_selects.db_fields import (
    ChainedForeignKey,
    ChainedManyToManyField,
    GroupedForeignKey,
    )

# Create your models here.


POSITIONS = (
    ('GK', 'Goalkeeper'),
    ('CB', 'Center fullback'),
    ('SW', 'Sweeper'),
    ('LFB', 'Left fullback'),
    ('RFB', 'Right fullback'),
    ('WB', 'Wingback'),
    ('LM', 'Left midfield'),
    ('RM', 'Right midfield'),
    ('DM', 'Defensive midfield'),
    ('CM', 'Center midfield'),
    ('WM', 'Wide midfield'),
    ('CF', 'Center forward'),
    ('AM', 'Attacking midfield'),
    ('S', 'Striker'),
    ('SS', 'Second striker'),
    ('LW', 'Left winger'),
    ('RW', 'Right winger'),
    )

CAF_LEVEL=(
    ('Beginner', 'Beginner'),
    ('FUFA level 1', 'FUFA level 1'),
    ('CAF C Diploma', 'CAF C Diploma'),
    ('CAF B Diploma', 'CAF B Diploma'),
    ('CAF A Diploma', 'CAF A Diploma'),
)

REF_LEVEL =(
    ('Beginner', 'Beginner'),
    (' level 3', 'FiFA level 3'),
    (' level 2', 'FiFA level 2'),
    (' level 1', 'FiFA level 1'),
)

REF_POSITION =(
    ('','' ),
    ('AR','Assistant Refereee'),
    ('CR','Centre Referee'),
    ('MC','Match Comm')
)

class County(models.Model):
    county_name = CaseInsensitiveCharField(max_length = 15,
        unique = True)
    def __str__(self):
        return self.county_name

    class Meta:
        verbose_name = 'County'
        verbose_name_plural = 'Counties'

class SubCounty (models.Model):
    sub_county_name = CaseInsensitiveCharField(max_length = 15,
        unique = True)
    county = models.ForeignKey(County, 
        on_delete=models.CASCADE)
    def __str__(self):
        return self.sub_county_name
    
    class Meta:
        verbose_name = 'Sub County'
        verbose_name_plural = 'Sub Counties'
    
class Ref (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='ref')
    avatar = models.ImageField(default='profile.png', 
        upload_to='ref_images')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    id_No = models.PositiveIntegerField(unique=True)
    birth_date = models.DateField()
    ref_level= models.CharField(choices=REF_LEVEL, 
        max_length=15, default='Beginner')
    position= models.CharField(choices=REF_POSITION,
        max_length=15, default='')
    county = models.ForeignKey(County,
        on_delete=models.SET_NULL, null=True)
    sub_county = ChainedForeignKey(
        "SubCounty",
        chained_field="county",
        chained_model_field="county",
        show_all=False,
        auto_choose=True,
        )
    class Meta:
        verbose_name = 'Referee'
        verbose_name_plural = 'Referees'
    @property
    def age(self):
        return int((datetime.now().date() 
        - self.birth_date).days / 365.25)
    
    def get_absolute_url(self):
        return reverse('team_details', 
            args=[str(self.id)])
            
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        #Returns the person's full name.
        return f'{self.first_name} {self.last_name}'



class Coach (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='coach')
    avatar = models.ImageField(default='profile.png', 
        upload_to='coach_images')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    id_No = models.PositiveIntegerField(unique=True)
    birth_date = models.DateField()
    caf_level= models.CharField(choices=CAF_LEVEL, 
        max_length=15, default='Beginner')
    county = models.ForeignKey(County,
        on_delete=models.SET_NULL, null=True)
    sub_county = ChainedForeignKey(
        "SubCounty",
        chained_field="county",
        chained_model_field="county",
        show_all=False,
        auto_choose=True,
        )
    class Meta:
        verbose_name = 'Coach'
        verbose_name_plural = 'Coaches'
    @property
    def age(self):
        return int((datetime.now().date() 
        - self.birth_date).days / 365.25)
    
    def get_absolute_url(self):
        return reverse('team_details', 
            args=[str(self.id)])
            
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        #Returns the person's full name.
        return f'{self.first_name} {self.last_name}'


class Team (models.Model):
    logo = models.ImageField(default='team_logo.png',
        upload_to='team_logos',)
    team_name = CaseInsensitiveCharField(max_length = 15,
        unique = True)
    short_name = models.CharField(max_length=50, null=True, verbose_name=_('Team short name'))
    slug = models.SlugField(unique=True, null=True, verbose_name=_('Slug'))
    team_manager = models.OneToOneField(User,
        on_delete=models.CASCADE,
        )
    coach= models.OneToOneField(Coach,
        on_delete=models.SET_NULL,related_name='coach', null=True
        )
    
    location_name = models.CharField(max_length = 15,
        )
    county = models.ForeignKey(County,
        on_delete=models.SET_NULL, null=True)
    sub_county = ChainedForeignKey(
        "SubCounty",
        chained_field="county",
        chained_model_field="county",
        show_all=False,
        auto_choose=True,
    )
     
    
    def __str__(self):
        return self.team_name
    def get_absolute_url(self):
        return reverse('team_details', 
            args=[str(self.id)])
    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.logo.path)
        
        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.logo.path)
    
class PlayerManager(models.Manager):
    use_for_related_fields = True

    def add_player(self, user, team):
        # ... your code here ...
        pass

    def remove_player(self, user, team):
        # ... your code here ...
        pass

    def transfer_player(self, user, team):
        # ... your code here ...
        #player_current_team = query player and display his team
        #player_new_team= query team (based on team name and fetch id)
        # player.team = player_new_team (by is Id)
        pass

    
         
class Player (models.Model):
    avatar = models.ImageField(default='player.jpg', 
    upload_to='players_images')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    id_birth_cert_no = models.PositiveIntegerField(unique=True)
    birth_date = models.DateField()
    county = models.ForeignKey(County,
        on_delete=models.SET_NULL, null=True)
    sub_county = ChainedForeignKey(
        "SubCounty",
        chained_field="county",
        chained_model_field="county",
        show_all=False,
        auto_choose=True,
    )
    position = models.CharField(choices=POSITIONS, 
        max_length=3)
    team = models.ForeignKey(Team, 
        related_name='player', on_delete=models.CASCADE)
    
    @property
    def age(self):
        return int((datetime.now().date() 
        - self.birth_date).days / 365.25)
    def get_absolute_url(self):
        return reverse('team_details', 
            args=[str(self.id)])
            
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        #Returns the person's full name.
        return self.first_name
    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


