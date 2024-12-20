"""
URL configuration for project project.

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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from app.views import SignUp
from app.forms import CustomLoginForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("app.urls")),
    path("signup/", SignUp.as_view(), name = "signup"),
    path("login/", LoginView.as_view(template_name = "app/auth/login.html", authentication_form = CustomLoginForm), name = "login"),
    path("logout/", LogoutView.as_view(), name = "logout"),
    path("<int:id>/password/", PasswordChangeView.as_view(template_name = "app/change_password.html"), name = "change-password"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
