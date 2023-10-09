"""
URL configuration for currency_alert project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Main.views import front,signup,currency,send_Mail,convert,alert,create_alert,screen,threshold,run,forgot_password,password_reset_email,password_reset_confirm,nice,nice1
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',front,name="front"),
    path('signup/',signup,name='signup'),
    path('currency/<int:user_id>',currency,name='currency'),
    path('send_mail/',send_Mail,name='send_Mail'),
    path('convert/<int:user_id>',convert,name='convert'),
    path('alert/',alert,name='alert'),
    path('create_alert/',create_alert,name='create_alert'),
    path('screen/',screen,name="screen"),
    path('threshold/<int:user_id>/',threshold,name="threshold"),
    path('run/<int:user_id>/',run,name="run"),
    path('forgot_password',forgot_password,name="forgot_password"),
    path('password_reset_email',password_reset_email,name="password_reset_email"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('nice/',nice,name='nice'),
    path('nice1/',nice1,name='nice1'),
]
