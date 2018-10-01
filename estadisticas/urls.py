from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from estadisticas import views

urlpatterns = [
    url(r'^estadisticas/$', views.estadistica_list),
    url(r'^estadisticas/(?P<pk>[0-9]+)/$', views.estadistica_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)