from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from teams.fields import CaseInsensitiveCharField
from teams.models import County,SubCounty
from datetime import date, datetime
from smart_selects.db_fields import (
    ChainedForeignKey,
    ChainedManyToManyField,
    GroupedForeignKey,
    )

# Create your models here.

class Branch(models.Model):
    name=CaseInsensitiveCharField(max_length=100, unique=True)
    county = models.OneToOneField(County, on_delete=models.SET_NULL,null=True)
    chairman = models.OneToOneField(User, on_delete=models.SET_NULL,
        related_name='branch_chairman', null=True)
    secretary= models.OneToOneField(User, on_delete=models.SET_NULL,
        related_name='branch_secretary',null=True)
    
    def __str__(self) -> str:
        return f'{self.name}'
    class Meta:
        verbose_name = 'branch'
        verbose_name_plural = 'branches'

class SubBranch(models.Model):
    name=CaseInsensitiveCharField(max_length=100, unique=True)
    branch= models.ForeignKey(Branch,on_delete=models.CASCADE,)
    chairman = models.OneToOneField(User, on_delete=models.SET_NULL,
        related_name='sub_branch_chairman', null=True)
    secretary= models.OneToOneField(User, on_delete=models.SET_NULL,
        related_name='sub_branch_secretary',null=True)
    
    def __str__(self) -> str:
        return f'{self.branch} {self.name}'

    class Meta:
        verbose_name = 'sub branch'
        verbose_name_plural = 'sub branches'


