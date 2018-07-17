import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from account.factories import AuthUserInteractorFactory
from PayDevs import settings


class ViewWrapper(View):

    view_factory = None

    def get(self, request, *args, **kwargs):
        kwargs.update(request.POST.dict())
        logged_user_id = self.auth_get_user(request)
        kwargs.update({'user_id': logged_user_id, 'project_id': request.META.get('HTTP_PROJECT')})
        body, status = self.view_factory().get(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    def post(self, request, *args, **kwargs):
        kwargs.update(request.POST.dict())
        json_data = json.loads(str(request.body, encoding='utf-8'))
        kwargs.update(json_data)
        kwargs.update({'secret_key': settings.SECRET_KEY})
        logged_user_id = self.auth_get_user(request)
        kwargs.update({'user_id': logged_user_id, 'project_id': request.META.get('HTTP_PROJECT')})
        body, status = self.view_factory().post(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')



    def auth_get_user(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header is None:
            return None
        token = auth_header.replace('Token ', '')
        logged_id = AuthUserInteractorFactory().create().set_params(token=token,
                                                                    secret_key=settings.SECRET_KEY).execute()
        return logged_id


# def index(request):
#     return render(request, 'index.html')
#
# def login(request):
#     return render(request, 'login.html')
#
# def create_project(request):
#     return render(request, 'create_project.html')