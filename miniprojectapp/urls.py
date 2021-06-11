<<<<<<< HEAD
from . import views
from django.urls import path
from django.contrib import admin
from miniprojectapp.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('index/',views.signup,name='signup'),
    path('login/',views.login1, name='login1'),
	path('login2/',views.login2, name='login2'),


	path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
	path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
	path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
	path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete')
=======
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index')
>>>>>>> a8d1b39ecf4ea0a8bd1f01783c19247e14f1c514
]