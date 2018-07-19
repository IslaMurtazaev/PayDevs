import json

from django.http import HttpResponse
from django.views import View

from account.factories import AuthUserInteractorFactory
from PayDevs import settings


class ViewWrapper(View):

    view_factory = None

    def get(self, request, *args, **kwargs):
        kwargs.update(request.GET.dict())
        kwargs.update(self.params(request))
        body, status = self.view_factory().get(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')


    def post(self, request, *args, **kwargs):
        kwargs.update(self.params(request))
        try:
            json_data = json.loads(str(request.body, encoding='utf-8'))
        except:
            json_data = request.POST.dict()

        kwargs.update(json_data)
        body, status = self.view_factory().post(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')


    def put(self, request, *args, **kwargs):
        kwargs.update(self.params(request))
        try:
            json_data = json.loads(str(request.body, encoding='utf-8'))
        except:
            json_data = request.POST.dict()

        kwargs.update(json_data)
        body, status = self.view_factory().put(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')


    def delete(self, request, *args, **kwargs):
        kwargs.update(self.params(request))
        try:
            json_data = json.loads(str(request.body, encoding='utf-8'))
        except:
            json_data = request.POST.dict()

        kwargs.update(json_data)
        body, status = self.view_factory().delete(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')



    def auth_get_user(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header is None:
            return None
        token = auth_header.replace('Token ', '')
        logged_id = AuthUserInteractorFactory().create().set_params(token=token,
                                                                    secret_key=settings.SECRET_KEY).execute()
        return logged_id


    def params(self, request):
        logged_user_id = self.auth_get_user(request)
        return {
                    'user_id': logged_user_id,
                    'project_id': request.META.get('HTTP_PROJECT'),
                    'task_id': request.META.get('HTTP_TASK'),
                    'hour_payment_id': request.META.get('HTTP_HOURPAYMENT'),
                    'month_payment_id': request.META.get('HTTP_MONTHPAYMENT'),
                    'work_day_id': request.META.get('HTTP_WORKDAY'),
                    'work_time_id': request.META.get('HTTP_WORKTIME'),
                    'secret_key': settings.SECRET_KEY
                }

    def get_params(self, request):
        pass

    def post_params(self, request):
        pass
