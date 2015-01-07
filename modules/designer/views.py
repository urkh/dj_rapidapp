from django.views.generic import TemplateView
from django.http import HttpResponse
import re
import json


def to_snakec(text):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def to_camelc(text):
    return text.title().replace(' ', '').replace('_', '')


def val_attrs(attr):

    attributes = ''
    size = '' if attr['size'] == '' else 'max_length=' + attr['size']
    cons_unique = 'unique=True' if 'UNIQUE' in attr['constraints'] else 'unique=False'
    cons_null = 'null=False' if 'NOT NULL' in attr['constraints'] else 'null=True'
    cons_blank = 'blank=False' if 'NOT NULL' in attr['constraints'] else 'blank=True'

    if attr['type'] == 'CharField':

        attributes = attr['type'] + '('
        attributes += cons_unique + ', '
        attributes += cons_blank + ', '
        attributes += cons_null + ', '
        attributes += 'db_column="' + attr['name'] + '", '
        attributes += 'verbose_name="' + attr['name'] + '", '
        attributes += size
        attributes += ')'

    elif attr['type'] == 'IntegerField':

        attributes = attr['type'] + '('
        attributes += cons_unique + ', '
        attributes += cons_blank + ', '
        attributes += cons_null + ', '
        attributes += 'db_column="' + attr['name'] + '", '
        attributes += 'verbose_name="' + attr['name'] + '", '
        attributes += size
        attributes += ')'

    elif attr['type'] == 'TextField':

        attributes = attr['type'] + '('
        attributes += cons_unique + ', '
        attributes += cons_blank + ', '
        attributes += cons_null + ', '
        attributes += 'db_column="' + attr['name'] + '", '
        attributes += 'verbose_name="' + attr['name'] + '", '
        attributes += size
        attributes += ')'

    return attributes


def set_attrs(attr):

    attributes = ''

    if attr['name'] != 'id':
        # import ipdb; ipdb.set_trace()
        attributes = '\n    ' + to_snakec(attr['name']) + ' = models.' + val_attrs(attr)

    return attributes


def designer_create(request):
    data = json.loads(request.body)

    tables = data['tables']
    # project_name = data['name']
    fw = open('models_test.py', 'w')
    fw.write('from django.db import models')

    for table in tables:
        fw.write('\n\n\nclass ' + to_camelc(table['name']) + '(models.Model):')

        # import ipdb; ipdb.set_trace()
        for attr in table['attributes']:

            fw.write(set_attrs(attr))

    fw.close()

    return HttpResponse(data, content_type='application/json; charset=utf-8')


class CreatorView(TemplateView):
    template_name = "designer.html"
