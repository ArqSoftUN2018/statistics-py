from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from tareas import views

urlpatterns = [
    url(r'^tareas/$', views.tarea_list),
    url(r'^tareas/(?P<pk>[0-9]+)/$', views.tarea_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)