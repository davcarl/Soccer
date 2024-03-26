from django.contrib import admin
from .models import County, Ref, SubCounty, Team, Player, Coach
# Register your models here
admin.site.register(County)
admin.site.register(SubCounty)
admin.site.register(Coach)
admin.site.register(Ref)