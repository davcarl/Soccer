from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.auth.models import User, auth
from django.views import View
from django.contrib.auth import views as auth_views
from .forms import RegisterForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UpdateProfileForm
from django.contrib.auth.views import PasswordChangeView


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(
            request.POST, instance=request.user)
        profile_form = UpdateProfileForm(
            request.POST, request.FILES, 
            instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,
            'Your profile is updated successfully')
            return redirect(to='profile_view')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'registeration/profile.html', {
        'user_form': user_form, 'profile_form': profile_form})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'registeration/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')
    
@login_required
def ProfileView(request):
    return render (request, 'registeration/profile_view.html')

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'registeration/registeration.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})

class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'registeration/password_reset.html'
    email_template_name = 'registeration/password_reset_email.html'
    subject_template_name = 'registeration/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')
