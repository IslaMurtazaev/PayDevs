from django.urls import path

from PayDevs.views import ViewWrapper
from project.factories.view_factories import *


urlpatterns = [

    path('create', ViewWrapper.as_view(view_factory=create_project_factory), name='create_project'),

    path('<int:project_id>', ViewWrapper.as_view(view_factory=get_project_factory), name='get_project'),

    path('<int:project_id>/update', ViewWrapper.as_view(view_factory=update_project_factory), name='update_project'),

    path('<int:project_id>/delete', ViewWrapper.as_view(view_factory=delete_project_factory), name='delete_project'),

    path('all', ViewWrapper.as_view(view_factory=get_projects_all_factory), name='get_all_projects'),

    path('<int:project_id>/total', ViewWrapper.as_view(view_factory=get_total_factory), name='get_project_total'),



    path('<int:project_id>/task/create', ViewWrapper.as_view(
        view_factory=create_task_factory), name='create_task'),

    path('<int:project_id>/task/<int:task_id>', ViewWrapper.as_view(
        view_factory=get_task_factory), name='get_task'),

    path('<int:project_id>/task/<int:task_id>/update', ViewWrapper.as_view(
        view_factory=update_task_factory), name='update_task'),

    path('task/<int:task_id>/delete', ViewWrapper.as_view(
        view_factory=delete_task_factory), name='delete_task'),

    path('<int:project_id>/task/all', ViewWrapper.as_view(
        view_factory=get_all_tasks_factory), name='get_all_tasks'),



    path('<int:project_id>/month_payment/create', ViewWrapper.as_view(
        view_factory=create_month_payment_factory), name='create_month_payment'),

    path('month_payment/<int:month_payment_id>', ViewWrapper.as_view(
        view_factory=get_month_payment_factory), name='get_month_payment'),

    path('<int:project_id>/month_payment/<int:month_payment_id>/update',
         ViewWrapper.as_view(view_factory=update_month_payment_factory), name='update_month_payment'),

    path('month_payment/<int:month_payment_id>/delete',
         ViewWrapper.as_view(view_factory=delete_month_payment_factory), name='delete_month_payment'),

    path('<int:project_id>/month_payment/all',
         ViewWrapper.as_view(view_factory=get_all_month_payments_factory), name='get_all_month_payments'),



    path('<int:project_id>/month_payment/<int:month_payment_id>/worked_day/create',
         ViewWrapper.as_view(view_factory=create_worked_day_factory), name='create_worked_day'),

    path('worked_day/<int:worked_day_id>',
         ViewWrapper.as_view(view_factory=get_worked_day_factory), name='get_worked_day'),

    path('<int:project_id>/month_payment/<int:month_payment_id>/worked_day/<int:worked_day_id>/update',
         ViewWrapper.as_view(view_factory=update_worked_day_factory), name='update_worked_day'),

    path('worked_day/<int:worked_day_id>/delete',
         ViewWrapper.as_view(view_factory=delete_worked_day_factory), name='delete_worked_day'),

    path('month_payment/<int:month_payment_id>/worked_day/all',
         ViewWrapper.as_view(view_factory=get_all_worked_days_factory), name='get_all_worked_days'),



    path('<int:project_id>/hour_payment/create',
         ViewWrapper.as_view(view_factory=create_hour_payment_factory), name='create_hour_payment'),

    path('hour_payment/<int:hour_payment_id>',
         ViewWrapper.as_view(view_factory=get_hour_payment_factory), name='get_hour_payment'),

    path('<int:project_id>/hour_payment/<int:hour_payment_id>/update',
         ViewWrapper.as_view(view_factory=update_hour_payment_factory), name='update_hour_payment'),

    path('hour_payment/<int:hour_payment_id>/delete',
         ViewWrapper.as_view(view_factory=delete_hour_payment_factory), name='delete_hour_payment'),

    path('<int:project_id>/hour_payment/all',
         ViewWrapper.as_view(view_factory=get_all_hour_payment_factory), name='get_all_hour_payments'),



    path('<int:project_id>/hour_payment/<int:hour_payment_id>/work_time/create',
         ViewWrapper.as_view(view_factory=create_work_time_factory), name='create_work_time'),

    path('work_time/<int:work_time_id>',
         ViewWrapper.as_view(view_factory=get_work_time_factory), name='get_work_time'),

    path('<int:project_id>/hour_payment/<int:hour_payment_id>/work_time/<int:work_time_id>/update',
         ViewWrapper.as_view(view_factory=update_work_time_factory), name='update_work_time'),

    path('work_time/<int:work_time_id>/delete',
         ViewWrapper.as_view(view_factory=delete_work_time_factory), name='delete_work_time'),

    path('hour_payment/<int:hour_payment_id>/work_time/all',
         ViewWrapper.as_view(view_factory=get_all_work_time_factory), name='get_all_work_time')
]
