from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from sampleapp import views
from sampleapp.views import ListWizard
from sampleapp.forms import ListForm

urlpatterns = patterns('',
    url(r'^login/', login_required(direct_to_template), {'template': 'login.html'}),
    url(r'^$', views.index, name='index'),
    url(r'^list/new/$', ListWizard.as_view([ListForm])),
    url(r'^list/edit/(?P<list_id>\d+)/$', views.edit, {}, 'list_edit'),
    url(r'^list/(?P<list_id>\d+)/$', views.listdetail, name='listdetail'),
    )
