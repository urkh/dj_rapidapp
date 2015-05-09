from django.views.generic import TemplateView
from django.http import HttpResponse
import os
import re
import json
import shutil
from modules.designer.build_project import set_settings, set_urls, set_wsgi, set_manage
from django.views.decorators.csrf import csrf_exempt


def make_projects(data):
    user_id = 'urkh'
    project_name = 'my_project'  # data['name']
    dbms = 'mysql'
    debug = True
    template_debug = True
    language = 'en-us'
    tables = data['tables']
    apps_name = []

    path_base = 'files/make_projects/'
    path_root = path_base + user_id + '/' + project_name
    path_settings = path_root + "/" + project_name
    path_modules = path_root + "/" + "modules"

    try:
        shutil.rmtree(path_base + user_id)
    except Exception:
        "No exist directory"

    os.makedirs(path_settings)
    os.mkdir(path_modules)

    for table in tables:

        path_app = path_modules + "/" + table['app_name']

        if not os.path.exists(path_app):
            os.mkdir(path_app)

        fw = open(path_app + '/__init__.py', 'a')
        fw.write("")
        fw.close()

        fw = open(path_app + '/admin.py', 'a')
        fw.write("")
        fw.close()

        fw = open(path_app + '/views.py', 'a')
        fw.write("")
        fw.close()

        fw = open(path_app + '/models.py', 'a')

        if table['app_name'] not in apps_name:
            fw.write('from django.db import models')
            apps_name.append(table['app_name'])

        fw.write('\n\n\nclass ' + to_camelc(table['name']) + '(models.Model):')

        for attr in table['attributes']:

            fw.write(set_attrs(attr))

        fw.close()

    # import ipdb; ipdb.set_trace()

    fw = open(path_settings + '/__init__.py', 'w')
    fw.write("")

    fw = open(path_settings + '/settings.py', 'w')
    fw.write(set_settings(project_name, apps_name, dbms, debug, template_debug, language))

    fw = open(path_settings + '/urls.py', 'w')
    fw.write(set_urls())
    fw.close()

    fw = open(path_settings + '/wsgi.py', 'a')
    fw.write(set_wsgi(project_name))
    fw.close()

    fw = open(path_root + '/manage.py', 'w')
    fw.write(set_manage(project_name))
    fw.close()

    fw = open(path_modules + '/__init__.py', 'w')
    fw.write("")
    fw.close()


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

    elif attr['type'] == 'ForeignKey':

        # import ipdb; ipdb.set_trace()
        attributes = attr['type'] + '('
        attributes += to_camelc(attr['name']) + ', '
        attributes += cons_blank + ', '
        attributes += cons_null + ', '
        attributes += 'verbose_name="' + attr['name'] + '", '
        attributes += ')'

    return attributes


def set_attrs(attr):

    attributes = ''

    if attr['name'] != 'id':
        # import ipdb; ipdb.set_trace()
        attributes = '\n    ' + to_snakec(attr['name']) + ' = models.' + val_attrs(attr)

    return attributes



@csrf_exempt
def designer_create(request):
    data = json.loads(request.body)

    # import ipdb; ipdb.set_trace()
    make_projects(data)

    return HttpResponse(data, content_type='application/json; charset=utf-8')


class CreatorView(TemplateView):
    template_name = "designer.html"
