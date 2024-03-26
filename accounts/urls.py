from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, RegisterView, ProfileView
from .views import ResetPasswordView, ChangePasswordView, profile
from .forms import LoginForm


urlpatterns = [
 
    path("register/", RegisterView.as_view(), 
        name="register"),
        
    path('password-change/', 
        ChangePasswordView.as_view(), 
        name='password_change'),
        
    path('login/', CustomLoginView.as_view(
            redirect_authenticated_user=True,
            template_name='registeration/login.html',
            authentication_form=LoginForm), name='login'),

    path('password-reset/', ResetPasswordView.as_view(), 
            name='password_reset'),
    
    path('profile/', profile, name='profile'),
    path('profile_view/',ProfileView, name='profile_view'),
    
    path('logout/', auth_views.LogoutView.as_view(
            template_name='registeration/logout.html'), name='logout'),
    
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
            template_name='registeration/password_reset_complete.html'),
            name='password_reset_complete'),
    path('password-reset-confirm/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(
            template_name='registeration/password_reset_confirm.html'),
            name='password_reset_confirm'),
    path('password-reset/', ResetPasswordView.as_view(),
        name='password_reset'),
    ]