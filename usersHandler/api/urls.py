
from django.urls import path
from django.contrib.auth import views as auth_views

from usersHandler.api.views import CustomAuthToken, log_out, registration_view, ChangePasswordView
urlpatterns = [
     path('login/', CustomAuthToken.as_view(), name='login'),
     path('logout/', log_out, name='logout'),
      path('register/', registration_view, name='register'),

     path('reset_password/',
         auth_views.PasswordResetView.as_view(), #if you want your persional template then just creace one and put link to as_view(template_name="path to templlate")
         name="reset_password"),

     path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),

     path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),

     path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),
         
]
