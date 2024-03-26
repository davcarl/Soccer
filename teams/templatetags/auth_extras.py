from django import template 
from django.contrib.auth.models import Group
register = template.Library() 

@register.filter(name = 'has_group') 
def has_group(user, group_name): 
    return user.groups.filter(
        name = group_name).exists()

def has_object(user, object):
    return Team.filter(
        team_manager = user).exists()

@register.filter
def in_category(things, category):
    return things.filter(category=category)