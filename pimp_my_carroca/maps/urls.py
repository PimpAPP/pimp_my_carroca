from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^hallo$', views.hallo),
    url(r'^show_maps$', views.show_maps),
    url(r'^new_form$', views.new_form),
    url(r'^form_receiver$', views.form_receiver)
)
