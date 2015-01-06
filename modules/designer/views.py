from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.


def designer_create(request):
    response = request.body
    print response
    #import ipdb; ipdb.set_trace()
    return HttpResponse(response, content_type='application/json; charset=utf-8')


class CreatorView(TemplateView):
    template_name = "designer.html"
    #model = Cliente

    #import ipdb; ipdb.set_trace()
