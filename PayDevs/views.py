import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class ViewWrapper(View):

    view_factory = None

    def get(self, request, *args, **kwargs):
        kwargs.update(request.POST.dict())
        body, status = self.view_factory().get(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    def post(self, request, *args, **kwargs):
        kwargs.update(request.POST.dict())
        body, status = self.view_factory().post(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')


def index(request):
    return render(request, 'index.html')



def login(request):
    return render(request, 'login.html')

def get_project(request):
    return render(request, 'get_project.html')