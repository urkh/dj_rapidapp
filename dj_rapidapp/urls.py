from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from modules.designer.views import CreatorView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', CreatorView.as_view(), name="creator_view"),
    url(r'^designer/create/$', 'modules.designer.views.designer_create', name="designer_create"),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
