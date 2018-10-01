from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from reportes import views

urlpatterns = [
    url(r'^reportes/$', views.reporte_list),
    url(r'^reportes/(?P<pk>[0-9]+)/$', views.reporte_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)