
from audioop import alaw2lin
from django.contrib import messages
from django.views import View

from branch.models import Branch
from .forms import TeamForm, PlayerForm, CoachForm,RefForm
from django.shortcuts import (render, 
    get_object_or_404,redirect)
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, FormView,
    CreateView, UpdateView, DeleteView,
    TemplateView
    )
from .models import *
from league.models import League
from branch.models import Branch,SubBranch
class Home(TemplateView):
    template_name= 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all()
        context['players']= Player.objects.all()
        context['leagues'] = League.objects.all()
        context['branches'] = Branch.objects.all()
        context['sub_branches'] = SubBranch.objects.filter()
        return context

class RefView (ListView):
    model= Ref
    template_name ='ref.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['refs'] = Ref.objects.all()
        return context

class CreateRefView(CreateView):
    model= Ref
    template_name = 'ref/create_ref.html'
    form_class = RefForm
    
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            Ref= form.save(commit=False)
            Ref.user = request.user
            Ref.avatar = request.user.profile.avatar
            Ref.first_name = request.user.first_name
            Ref.last_name = request.user.last_name
            Ref.save()
            name = form.cleaned_data.get('first_name','last_name')
            messages.success(request, f'Ref {name} created')
            return redirect(to='ref')
        else:
            return render(request, self.template_name, {'form': form})

class RefDetailView(DetailView):
    model = Ref
    template_name= 'ref/ref_detail_view.html'

class UpdateRefView(UpdateView):
    model = Ref
    form_class = RefForm
    template_name = 'Ref/update_ref.html'

    def get_success_url(self):
        messages.success = 'Ref details updated'
        return reverse_lazy('ref')

class DeleteRefView(DeleteView):
    model = Ref
    template_name = 'ref/ref_view.html'
    success_message ="Ref deleted successfully"

    def get_success_url(self):
        messages.success = 'Ref deleted'
        return reverse_lazy('ref')

class CoachView (ListView):
    model= Coach
    template_name ='coach.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coaches'] = Coach.objects.all()
        return context

class CreateCoachView(CreateView):
    model= Coach
    template_name = 'coach/create_coach.html'
    form_class = CoachForm
    
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            coach= form.save(commit=False)
            coach.user = request.user
            coach.avatar = request.user.profile.avatar
            coach.first_name = request.user.first_name
            coach.last_name = request.user.last_name
            coach.save()
            name = form.cleaned_data.get('first_name','last_name')
            messages.success(request, f'coach {name} created')
            return redirect(to='coach')
        else:
            return render(request, self.template_name, {'form': form})

class CoachDetailView(DetailView):
    model = Coach
    template_name= 'coach/coach_detail_view.html'

class UpdateCoachView(UpdateView):
    model = Coach
    form_class = CoachForm
    template_name = 'coach/update_coach.html'

    def get_success_url(self):
        messages.success = 'coach details updated'
        return reverse_lazy('coach')

class DeleteCoachView(DeleteView):
    model = Coach
    template_name = 'coach/coach_view.html'
    success_message ="coach deleted successfully"

    def get_success_url(self):
        messages.success = 'Coach deleted'
        return reverse_lazy('coach')

class AddPlayerView(CreateView):
    model= Player
    template_name = 'teams/add_player.html'
    form_class = PlayerForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            player= form.save(commit=False)
            player.team = request.user.team
            player.save()
            name = form.cleaned_data.get('first_name','last_name')
            messages.success(request, f'player {name} created')
            return redirect(to='team_details', pk = player.team.pk)
        else:
            return render(request, self.template_name, {'form': form})

class PlayerDetailView(DetailView):
    model = Player
    template_name= 'teams/player_detail_view.html'

class UpdatePlayerView(UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'teams/edit_player.html'

    def get_success_url(self):
        messages.success = 'player details updated'
        return reverse_lazy('team_details', args=[str(self.object.team.id)])

class DeletePlayerView(DeleteView):
    model = Player
    template_name = 'teams/team_detail_view.html'
    success_message ="player deleted successfully"

    def get_success_url(self):
        messages.success = 'player deleted'
        return reverse_lazy('team_details', args=[str(self.object.team.id)])

class Teams(ListView):
    model= Team
    template_name= 'teams.html'

class CreateTeamView(FormView):
    model= Team
    template_name = 'teams/create_team.html'
    form_class = TeamForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        
        if form.is_valid():
            team=form.save (commit = False)
            try:
                team.team_manager = request.user
                team.save()
                team_name = form.cleaned_data.get('team_name')
                messages.success(request, f'created team {team_name}')
                return redirect(to = 'home')
            except:
                pass
        else:
            return render(request, self.template_name, {'form': form})

class TeamDetailView(DetailView):
    model = Team
    template_name= 'teams/team_detail_view.html'
    fields = ('logo','team_name','location_name','coach',
        'team_manager','county','sub_county')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['players'] = Player.objects.filter(team=self.object)
        
        return context

class TeamUpdateView(UpdateView):
    model = Team #model
    fields = ('logo','team_name','location_name', 
        'coach_name','county','sub_county')
    template_name = 'teams/update_team.html' # templete for updating
    def get_success_url(self):
        messages.success = 'team details updated'
        return reverse_lazy('team_details', kwargs={'pk': self.object.pk})

class DeleteTeamView(DeleteView):
    model = Team
    template_name = "teams/teams_base.html"
    success_message ="team deleted successfully"
    
    def get_success_url(self):
        messages.success = 'team deleted'
        return reverse_lazy('teams')
   

