import json

from django.http import HttpResponse
from django.views import View
from reportlab.pdfgen import canvas

from PayDevs.decorators import json_exception
from account.factories.interactor_factories import AuthUserInteractorFactory
from PayDevs import settings


class ViewWrapper(View):

    view_factory = None

    def get(self, request, *args, **kwargs):
        kwargs.update(request.GET.dict())
        kwargs.update(self.params(request))
        body, status = self.view_factory().get(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    @json_exception
    def post(self, request, *args, **kwargs):
        kwargs.update(self.params(request))
        json_data = json.loads(str(request.body, encoding='utf-8'))
        kwargs.update(json_data)
        body, status = self.view_factory().post(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    @json_exception
    def put(self, request, *args, **kwargs):
        kwargs.update(self.params(request))
        json_data = json.loads(str(request.body, encoding='utf-8'))
        kwargs.update(json_data)
        body, status = self.view_factory().put(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')


    def delete(self, request, *args, **kwargs):
        kwargs.update(self.params(request))
        body, status = self.view_factory().delete(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    @json_exception
    def patch(self, request, *args, **kwargs):
        kwargs.update(self.params(request))
        json_data = json.loads(str(request.body, encoding='utf-8'))
        kwargs.update(json_data)
        body, status = self.view_factory().patch(*args, **kwargs)
        return self.pdf_generator(body)




    def auth_get_user(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header is None:
            return None
        token = auth_header.replace('Token ', '')
        logged_id = AuthUserInteractorFactory().create().set_params(token=token,
                                                                    secret_key=settings.SECRET_KEY).execute()
        return logged_id


    def pdf_generator(self, body):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="bill.pdf"'

        p = canvas.Canvas(response)
        height = 700
        p.drawString(200, 800, "Project total report bill")
        for key in body:
            if key == 'type_of_payment':
                if body[key] == 'M_P':
                    body[key] = "Monthly payment"
                elif body[key] == 'H_P':
                    body[key] = "Hourly payment"
                else:
                    body[key] = "Tacky payment"
                p.drawString(150, height, "Type of payment: " + body[key])
            else:
                p.drawString(150, height, "%s:  %s" % (key.title(), body[key]))
            height -= 25
        p.showPage()
        p.save()

        return response


    def params(self, request):
        logged_user_id = self.auth_get_user(request)
        return {
                    'logged_id': logged_user_id,
                    'secret_key': settings.SECRET_KEY
                }

    def get_params(self, request):
        pass

    def post_params(self, request):
        pass
