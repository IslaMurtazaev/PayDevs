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

from PayDevs.views import ViewWrapper
from account.factories.view_factory import get_user_regist_factories, get_user_login_factories, \
    get_user_factories
from project.factories.view_factories import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/create', csrf_exempt(ViewWrapper.as_view(view_factory=get_user_regist_factories)), name='create_user'),
    path('users/login', csrf_exempt(ViewWrapper.as_view(view_factory=get_user_login_factories)), name='login_user'),
    path('users/', ViewWrapper.as_view(view_factory=get_user_factories), name='get_user'),

    path('project/create', csrf_exempt(ViewWrapper.as_view(view_factory=create_project_factory)), name='create_project'),
    path('project/all', ViewWrapper.as_view(view_factory=get_projects_all_factory), name='get_all_projects'),
    # path('project/total', ViewWrapper.as_view(view_factory=get_total_factory), name='get_total'),
    path('project/<int:project_id>/', ViewWrapper.as_view(view_factory=get_project_factory), name='get_project'),
    path('project/<int:project_id>/update/', csrf_exempt(ViewWrapper.as_view(view_factory=update_project_factory)),
         name='update_project'),
    path('project/<int:project_id>/delete/', csrf_exempt(ViewWrapper.as_view(view_factory=delete_project_factory)),
         name='delete_project'),

    path('project/<int:project_id>/task/create/', csrf_exempt(ViewWrapper.as_view(view_factory=create_task_factory)),
         name='create_task'),
    path('project/<int:project_id>/task/all/', ViewWrapper.as_view(view_factory=get_all_tasks_factory),
             name='get_all_tasks'),
    path('project/<int:project_id>/task/<int:task_id>/', ViewWrapper.as_view(view_factory=get_task_factory),
         name='get_task'),


    path('project/<int:project_id>/task/<int:task_id>/update/',
         csrf_exempt(ViewWrapper.as_view(view_factory=update_task_factory)),
         name='update_task'),
    path('project/<int:project_id>/task/<int:task_id>/delete/',
         csrf_exempt(ViewWrapper.as_view(view_factory=delete_task_factory)),
         name='delete_task'),

]
