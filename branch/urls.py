from django.urls import re_path, path

from .views import BranchDetail, BranchView 

urlpatterns = [
    path('branch/', BranchView.as_view(), name='branch'),
    path('branch/<int:pk>/', BranchDetail.as_view(), name='branch_details'),
    
]