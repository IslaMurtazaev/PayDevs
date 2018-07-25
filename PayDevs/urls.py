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




    path('project/<int:project_id>/', ViewWrapper.as_view(view_factory=get_project_factory), name='get_project'),
    path('project/<int:project_id>/update/', csrf_exempt(ViewWrapper.as_view(view_factory=update_project_factory)),
         name='update_project'),
    path('project/<int:project_id>/delete/', csrf_exempt(ViewWrapper.as_view(view_factory=delete_project_factory)),
         name='delete_project'),
    path('project/all', ViewWrapper.as_view(view_factory=get_projects_all_factory), name='get_all_projects'),


    path('project/<int:project_id>/task/create/', csrf_exempt(ViewWrapper.as_view(view_factory=create_task_factory)),
         name='create_task'),
    path('project/<int:project_id>/task/all/', ViewWrapper.as_view(view_factory=get_all_tasks_factory),
         name='get_all_tasks'),
    path('project/<int:project_id>/task/<int:task_id>/', ViewWrapper.as_view(view_factory=get_task_factory),
         name='get_task'),
    path('project/<int:project_id>/task/<int:task_id>/update/', csrf_exempt(ViewWrapper.as_view(view_factory=update_task_factory)),
         name='update_task'),
    path('project/<int:project_id>/task/<int:task_id>/delete/', csrf_exempt(ViewWrapper.as_view(view_factory=delete_task_factory)),
         name='delete_task'),


    path('project/<int:project_id>/monthpayment/create/', csrf_exempt(ViewWrapper.as_view(view_factory=create_month_payment_factory)),
         name='create_month_payment'),
    path('project/<int:project_id>/monthpayment/<int:month_payment_id>/', ViewWrapper.as_view(view_factory=get_month_payment_factory),
         name='get_month_payment'),
    path('project/<int:project_id>/monthpayment/<int:month_payment_id>/update/',
         csrf_exempt(ViewWrapper.as_view(view_factory=update_month_payment_factory)),
         name='update_month_payment'),
    path('project/<int:project_id>/monthpayment/<int:month_payment_id>/delete/',
         csrf_exempt(ViewWrapper.as_view(view_factory=delete_month_payment_factory)),
         name='delete_month_payment'),
    path('project/<int:project_id>/monthpayment/all/', ViewWrapper.as_view(view_factory=get_all_month_payments_factory),
         name='get_all_month_payments'),


    path('project/<int:project_id>/hour_payment/create/',
         csrf_exempt(ViewWrapper.as_view(view_factory=create_hour_payment_factory)), name='create_hour_payment'),

    path('project/<int:project_id>/hour_payment/all/',
         csrf_exempt(ViewWrapper.as_view(view_factory=get_all_hour_payment_factory)), name='get_all_hour_payment'),

    path('project/<int:project_id>/hour_payment/<int:hour_payment_id>/',
         csrf_exempt(ViewWrapper.as_view(view_factory=get_hour_payment_factory)), name='get_hour_payment'),

    path('project/<int:project_id>/hour_payment/<int:hour_payment_id>/update/',
         csrf_exempt(ViewWrapper.as_view(view_factory=update_hour_payment_factory)), name='update_hour_payment'),

    path('project/<int:project_id>/hour_payment/<int:hour_payment_id>/delete/',
         csrf_exempt(ViewWrapper.as_view(view_factory=delete_hour_payment_factory)), name='delete_hour_payment'),



    path('project/<int:project_id>/hour_payment/<int:hour_payment_id>/work_time/create',
         csrf_exempt(ViewWrapper.as_view(view_factory=create_work_time_factory)), name='create_work_time'),

    path('project/<int:project_id>/hour_payment/<int:hour_payment_id>/work_time/all',
         csrf_exempt(ViewWrapper.as_view(view_factory=get_all_work_time_factory)), name='get_all_work_time'),

    path('project/<int:project_id>/hour_payment/<int:hour_payment_id>/work_time/<int:work_time_id>',
         csrf_exempt(ViewWrapper.as_view(view_factory=get_work_time_factory)), name='get_work_time'),
    path('project/<int:project_id>/hour_payment/<int:hour_payment_id>/work_time/<int:work_time_id>/update',
             csrf_exempt(ViewWrapper.as_view(view_factory=update_work_time_factory)), name='update_work_time'),
    path('project/<int:project_id>/hour_payment/<int:hour_payment_id>/work_time/<int:work_time_id>/delete',
                 csrf_exempt(ViewWrapper.as_view(view_factory=delete_work_time_factory)), name='delete_work_time'),

]
