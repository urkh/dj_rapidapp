from django.utils.crypto import get_random_string


def set_manage(project_name):

    manage = ""
    manage += "#!/usr/bin/env python"
    manage += "\nimport os"
    manage += "\nimport sys"
    manage += "\n\nif __name__ == '__main__':"
    manage += "\n    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '" + project_name + ".settings')"
    manage += "\n    from django.core.management import execute_from_command_line"
    manage += "\n    execute_from_command_line(sys.argv)"

    return manage


def set_urls():

    urls = ""
    urls += "from django.conf.urls import patterns, include, url"
    urls += "\nfrom django.contrib import admin"
    urls += "\n\nurlpatterns = patterns('',"
    urls += "\n    url(r'^admin/', include(admin.site.urls)),"
    urls += "\n)"

    return urls


def set_wsgi(project_name):

    wsgi = ""
    wsgi += "import os"
    wsgi += "\nos.environ.setdefault('DJANGO_SETTINGS_MODULE', '" + project_name + ".settings')"
    wsgi += "\n\nfrom django.core.wsgi import get_wsgi_application"
    wsgi += "\napplication = get_wsgi_application()"

    return wsgi


def set_settings(project_name, app_name, dbms, debug, debug_template, language):

    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(50, chars)

    _debug = 'True' if debug else 'False'
    _debug_template = 'True' if debug_template else 'False'

    settings = "import os"
    settings += "\n\n\nBASE_DIR = os.path.dirname(os.path.dirname(__file__))"
    settings += "\nSECRET_KEY = '" + secret_key + "'"
    settings += "\nDEBUG = " + _debug
    settings += "\nTEMPLATE_DEBUG = " + _debug_template
    settings += "\nALLOWED_HOSTS = []"
    settings += "\nROOT_URLCONF = '" + project_name + ".urls'"
    settings += "\nWSGI_APPLICATION = '" + project_name + ".wsgi.application'"
    settings += "\nLANGUAGE_CODE = '" + language + "'"
    settings += "\nTIME_ZONE = 'UTC'"
    settings += "\nUSE_I18N = True"
    settings += "\nUSE_L10N = True"
    settings += "\nUSE_TZ = True"
    settings += "\nSTATIC_URL = '/static/'"

    settings += set_installed_apps(app_name)
    settings += set_middlewares()
    settings += set_database(dbms)

    return settings


def set_installed_apps(app_name):

    apps = "\n\nINSTALLED_APPS = ("
    apps += "\n    'django.contrib.admin',"
    apps += "\n    'django.contrib.auth',"
    apps += "\n    'django.contrib.contenttypes',"
    apps += "\n    'django.contrib.sessions',"
    apps += "\n    'django.contrib.messages',"
    apps += "\n    'django.contrib.staticfiles',"
    for app in app_name:
        apps += "\n    'modules." + app + "',"
    apps += "\n)"

    return apps


def set_middlewares():

    mids = "\n\nMIDDLEWARE_CLASSES = ("
    mids += "\n    'django.contrib.sessions.middleware.SessionMiddleware',"
    mids += "\n    'django.middleware.common.CommonMiddleware',"
    mids += "\n    'django.middleware.csrf.CsrfViewMiddleware',"
    mids += "\n    'django.contrib.auth.middleware.AuthenticationMiddleware',"
    mids += "\n    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',"
    mids += "\n    'django.contrib.messages.middleware.MessageMiddleware',"
    mids += "\n    'django.middleware.clickjacking.XFrameOptionsMiddleware',"
    mids += "\n)"

    return mids


def set_database(dbms):

    db = "\n\nDATABASES = {"
    db += "\n'default': {"
    db += "\n    'ENGINE': 'django.db.backends.sqlite3',"
    db += "\n    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),"
    db += "\n}"

    return db
