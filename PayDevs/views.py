import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class ViewWrapper(View):

    view_factory = None

    def get(self, request, *args, **kwargs):
        body, status = self.view_factory().get(**kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    def post(self, request, *args, **kwargs):
        body, status = self.view_factory().post(request, *args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')


def index(request):
    return render(request, 'index.html')



def login(request):
    return render(request, 'login.html')