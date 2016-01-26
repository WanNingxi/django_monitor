from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^index$', views.index),
	url(r'^show_author$', views.show_author),
]
