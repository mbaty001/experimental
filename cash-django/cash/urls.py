from django.conf.urls import url

from . import views

urlpatterns = [
    # /cash
    url(r'^$', views.index, name='index'),
    # /cash/stats
    url(r'stats/$', views.stats, name='stats'),
    # /cash/stats/precision-10
    url(r'stats/(?:precision-(?P<precision>\d+)/)?$', views.stats, name='stats'),
]

