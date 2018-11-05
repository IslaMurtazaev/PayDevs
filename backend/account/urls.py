from django.urls import path

from PayDevs.views import ViewWrapper
from account.factories.view_factory import get_user_regist_factories, get_user_login_factories, \
    get_user_factories


urlpatterns = [
    path('create', ViewWrapper.as_view(view_factory=get_user_regist_factories), name='create_user'),
    path('login', ViewWrapper.as_view(view_factory=get_user_login_factories), name='login_user'),
    path('', ViewWrapper.as_view(view_factory=get_user_factories), name='get_user'),
]

