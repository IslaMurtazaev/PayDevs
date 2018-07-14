"""example_paydevs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.views.decorators.csrf import csrf_exempt

from account.factories import get_user_factories, get_user_all_factories, get_user_regist_factories, \
    get_user_login_factories
from project.factories import get_project_factory, create_project_factory, get_all_projects_factory
from PayDevs.views import ViewWrapper, index, login, create_project


urlpatterns = [
    path('create_user/', index),
    path('login_user/', login),
    path('admin/', admin.site.urls),
    path('users/all', ViewWrapper.as_view(view_factory=get_user_all_factories)),
    path('users/create', csrf_exempt(ViewWrapper.as_view(view_factory=get_user_regist_factories)), name='create_user'),
    path('users/login', csrf_exempt(ViewWrapper.as_view(view_factory=get_user_login_factories)), name='login_user'),
    path('users/<slug:username>', ViewWrapper.as_view(view_factory=get_user_factories)),
    
    path('create_project/', create_project),
    path('project/create', csrf_exempt(ViewWrapper.as_view(view_factory=create_project_factory)), name='create_project'),
    path('project/all', ViewWrapper.as_view(view_factory=get_all_projects_factory), name='get_all_projects'),
    path('project/<slug:title>', ViewWrapper.as_view(view_factory=get_project_factory), name='get_project'),
    # path('project/total/<slug:title>', ViewWrapper.as_view(view_factory=get_project_total_factory), name='get_total')
]
