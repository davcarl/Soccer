from audioop import alaw2lin
from django.contrib import messages
from django.views import View
from django.shortcuts import (render, 
    get_object_or_404,redirect)
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, FormView,
    CreateView, UpdateView, DeleteView,
    TemplateView
    )
from django.shortcuts import render
from .models import Branch, SubBranch
from league.models import League
# Create your views here.

class BranchView(ListView):
    model = Branch
    template_name= 'branch/branch.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_branches'] = SubBranch.objects.all()
        return context

class BranchDetail(DetailView):
    model = Branch
    template_name= 'branch/branch_detail.html'
